from create_product.repository import save_product
from create_product.validators import validate_product_data
from common.exceptions import BadRequestException
from decimal import Decimal

def create_product_service(data):
    # Validar los datos del producto
    validate_product_data(data)
    
    # Procesar datos adicionales si es necesario
    product = {
        'id': generate_unique_id(),
        'name': data['name'],
        'category': data['category'],
        'price': Decimal(str(data['price'])),
        'stock': data.get('stock', 0)
    }

    # Guardar el producto en la base de datos
    save_product(product)

    return product

def generate_unique_id():
    # Generar un ID único para el producto
    import uuid
    return str(uuid.uuid4())
