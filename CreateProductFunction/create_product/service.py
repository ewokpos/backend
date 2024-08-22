from create_product.repository import ProductRepository
from common.exceptions import MissingFieldException, InvalidDataException

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def create_product(self, product_data):
        # Validar datos de entrada
        required_fields = {'name', 'category', 'price', 'stock', 'description', 'sku', 'barcode'}
        missing_fields = required_fields - product_data.keys()

        if missing_fields:
            raise MissingFieldException(missing_fields)
        
        try:
            return self.repository.create_product(product_data)
        except Exception as e:
            # Aquí se podría manejar más finamente según la excepción específica de la base de datos
            raise InvalidDataException(f"An error occurred: {str(e)}")
