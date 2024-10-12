from create_product.repository import SaleRepository
from common.exceptions import MissingFieldException, InvalidDataException

class SaleService:
    def __init__(self):
        self.repository = SaleRepository()

    def create_sale(self, sale_data):
        # Validar datos de entrada
        required_fields = {'customer_id', 'products', 'total_amount', 'payment_method'}
        missing_fields = required_fields - sale_data.keys()

        if missing_fields:
            raise MissingFieldException(missing_fields)
        
        try:
            return self.repository.create_sale(sale_data)
        except Exception as e:
            raise InvalidDataException(f"An error occurred: {str(e)}")
