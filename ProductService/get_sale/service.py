from create_sale.repository import SaleRepository
from common.exceptions import SaleNotFoundException

class SaleService:
    def __init__(self):
        self.repository = SaleRepository()

    def get_sale(self, sale_id):
        try:
            sale = self.repository.get_sale(sale_id)
            if not sale:
                raise SaleNotFoundException(f"Sale with ID {sale_id} not found")
            return sale
        except Exception as e:
            raise SaleNotFoundException(f"An error occurred: {str(e)}")
