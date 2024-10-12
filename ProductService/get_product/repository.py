from psycopg2 import sql
from common.exceptions import ProductNotFoundException
from database.connection_pool import DatabaseConnectionPool
from database.models import Product

class ProductRepository:
    def __init__(self):
        self.connection_pool = DatabaseConnectionPool()

    def get_product(self, product_id):
        conn = self.connection_pool.get_connection()
        try:
            with conn.cursor() as cursor:
                query = sql.SQL("SELECT * FROM ProductsTable WHERE id = %s")
                cursor.execute(query, (product_id,))
                result = cursor.fetchone()

                if result is None:
                    raise ProductNotFoundException(f"Product with ID {product_id} not found")

                product = Product(
                    id=result[0],
                    name=result[1],
                    category=result[2],
                    price=result[3],
                    stock=result[4],
                    description=result[5],
                    sku=result[6],
                    barcode=result[7]
                )
                return product.to_dict()
        finally:
            self.connection_pool.put_connection(conn)
