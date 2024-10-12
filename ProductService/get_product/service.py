from get_product.repository import ProductRepository
from common.exceptions import ProductNotFoundException

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def get_product(self, product_id):
        product = self.repository.get_product(product_id)
        if not product:
            raise ProductNotFoundException(f"Product with ID {product_id} not found")
        return product
