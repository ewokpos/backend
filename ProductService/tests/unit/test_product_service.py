import pytest
from unittest.mock import MagicMock, patch
from create_product.service import ProductService
from common.exceptions import MissingFieldException, InvalidDataException

@pytest.fixture
def mock_product_repository():
    return MagicMock()

@pytest.fixture
def product_service(mock_product_repository):
    with patch('create_product.service.ProductRepository', return_value=mock_product_repository):
        service = ProductService()
        return service, mock_product_repository

def test_create_product_success(product_service):
    service, mock_repository = product_service
    
    product_data = {
        'name': 'Test Product',
        'category': 'Test Category',
        'price': '9.99',
        'stock': 10,
        'description': 'A test product description',
        'sku': 'TESTSKU123',
        'barcode': '1234567890123'
    }
    
    mock_repository.create_product.return_value = {
        'id': 1,
        'name': 'Test Product',
        'category': 'Test Category',
        'price': '9.99',
        'stock': 10,
        'description': 'A test product description',
        'sku': 'TESTSKU123',
        'barcode': '1234567890123'
    }
    
    result = service.create_product(product_data)
    
    mock_repository.create_product.assert_called_once_with(product_data)
    assert result == {
        'id': 1,
        'name': 'Test Product',
        'category': 'Test Category',
        'price': '9.99',
        'stock': 10,
        'description': 'A test product description',
        'sku': 'TESTSKU123',
        'barcode': '1234567890123'
    }

def test_create_product_missing_fields(product_service):
    service, _ = product_service

    product_data = {
        'name': 'Test Product',
        'category': 'Test Category',
        'price': '9.99',
        'stock': 10,
        'description': 'A test product description'
    }
    
    with pytest.raises(MissingFieldException, match="Missing required fields: sku, barcode"):
        service.create_product(product_data)