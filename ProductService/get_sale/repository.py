from psycopg2 import sql
from common.exceptions import SaleNotFoundException
from database.connection_pool import DatabaseConnectionPool

class SaleRepository:
    def __init__(self):
        self.connection_pool = DatabaseConnectionPool()

    def get_sale(self, sale_id):
        conn = self.connection_pool.get_connection()
        try:
            with conn.cursor() as cursor:
                query = sql.SQL("SELECT * FROM SalesTable WHERE id = %s")
                cursor.execute(query, (sale_id,))
                sale = cursor.fetchone()
                if not sale:
                    raise SaleNotFoundException(f"Sale with ID {sale_id} not found")
                return sale
        finally:
            self.connection_pool.put_connection(conn)
