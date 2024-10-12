from delete_product.repository import ProductRepository  # Apunta al repository de delete_product
from common.exceptions import ProductNotFoundException, InvalidDataException

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def delete_product(self, product_id):
        # Llamar al repositorio para eliminar el producto
        try:
            self.repository.delete_product(product_id)
        except ProductNotFoundException:
            raise ProductNotFoundException(f"Product with ID {product_id} not found")
        except Exception as e:
            raise InvalidDataException(f"An error occurred: {str(e)}")
