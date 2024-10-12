from update_product.repository import ProductRepository  # Apunta al repository de update_product
from common.exceptions import MissingFieldException, ProductNotFoundException, InvalidDataException

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def update_product(self, product_id, product_data):
        # Validar que los campos necesarios estén presentes
        required_fields = {'name', 'category', 'price', 'stock', 'description', 'sku', 'barcode'}
        missing_fields = required_fields - product_data.keys()

        if missing_fields:
            raise MissingFieldException(missing_fields)
        
        # Llamar al repositorio para actualizar el producto
        try:
            return self.repository.update_product(product_id, product_data)
        except ProductNotFoundException:
            raise ProductNotFoundException(f"Product with ID {product_id} not found")
        except Exception as e:
            raise InvalidDataException(f"An error occurred: {str(e)}")
