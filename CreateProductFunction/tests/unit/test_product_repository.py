import pytest
from unittest.mock import MagicMock
from create_product.repository import ProductRepository
from common.exceptions import BadRequestException

@pytest.fixture
def product_repository():
    # Crear un mock del pool de conexiones
    mock_connection_pool = MagicMock()
    repository = ProductRepository()
    repository.connection_pool = mock_connection_pool
    return repository, mock_connection_pool

def test_create_product_success(product_repository):
    repository, mock_connection_pool = product_repository
    
    # Configurar el mock para devolver una conexión
    mock_conn = MagicMock()
    mock_connection_pool.get_connection.return_value = mock_conn
    
    # Configurar el cursor del mock
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    
    # Datos del producto para el test
    product_data = {
        'name': 'Test Product',
        'category': 'Test Category',
        'price': '9.99',
        'stock': 10,
        'description': 'A test product description',
        'sku': 'TESTSKU123',
        'barcode': '1234567890123'
    }
    
    # Configurar el cursor para devolver un ID
    mock_cursor.fetchone.return_value = [1]
    
    result = repository.create_product(product_data)
    
    # Verificar que el cursor ejecuta el SQL correcto
    mock_cursor.execute.assert_called_once()
    
    # Verificar que se ha hecho commit
    mock_conn.commit.assert_called_once()
    
    # Verificar el resultado
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

def test_create_product_missing_fields(product_repository):
    repository, _ = product_repository
    
    # Datos del producto con campos faltantes
    product_data = {
        'name': 'Test Product',
        'category': 'Test Category',
        'price': '9.99',
        'stock': 10,
        'description': 'A test product description'
    }
    
    # Verificar que se lanza una excepción cuando faltan campos
    with pytest.raises(BadRequestException, match="Missing required product fields"):
        repository.create_product(product_data)
