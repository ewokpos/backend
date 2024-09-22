import json
import pytest
from unittest.mock import patch
from create_product.handler import handler

@pytest.fixture
def mock_event():
    return {
        'body': json.dumps({
            'name': 'Test Product',
            'category': 'Test Category',
            'price': '9.99',  # Asegúrate de que el tipo coincida con lo esperado
            'stock': 10,
            'description': 'A test product description',
            'sku': 'TESTSKU123',
            'barcode': '1234567890123'
        })
    }

def test_lambda_creates_product(mock_event):
    with patch('create_product.service.ProductService') as MockService:
        mock_service = MockService.return_value
        mock_service.create_product.return_value = {
            'id': 1,
            'name': 'Test Product',
            'category': 'Test Category',
            'price': '9.99',
            'stock': 10,
            'description': 'A test product description',
            'sku': 'TESTSKU123',
            'barcode': '1234567890123'
        }

        response = handler(mock_event, None)
        
        assert response['statusCode'] == 201
        body = json.loads(response['body'])
        assert body['message'] == 'Product created successfully'
        
        # Verificar que los campos del producto están en la respuesta
        product = body['product']
        assert product['name'] == 'Test Product'
        assert product['category'] == 'Test Category'
        assert product['price'] == '9.99'
        assert product['stock'] == 10
        assert product['description'] == 'A test product description'
        assert product['sku'] == 'TESTSKU123'
        assert product['barcode'] == '1234567890123'
