from psycopg2 import sql
from common.exceptions import DatabaseError
from database.connection_pool import DatabaseConnectionPool

class SaleRepository:
    def __init__(self):
        self.connection_pool = DatabaseConnectionPool()

    def create_sale(self, sale_data):
        conn = self.connection_pool.get_connection()
        try:
            with conn.cursor() as cursor:
                query = sql.SQL("""
                    INSERT INTO SalesTable (customer_id, total_amount, payment_method)
                    VALUES (%s, %s, %s)
                    RETURNING id;
                """)
                cursor.execute(query, (
                    sale_data['customer_id'],
                    sale_data['total_amount'],
                    sale_data['payment_method']
                ))
                sale_id = cursor.fetchone()[0]
                conn.commit()
                return {'sale_id': sale_id}
        except Exception as e:
            raise DatabaseError(f"An error occurred during sale creation: {str(e)}")
        finally:
            self.connection_pool.put_connection(conn)
