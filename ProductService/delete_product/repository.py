from psycopg2 import sql
from common.exceptions import ProductNotFoundException, DatabaseError
from database.connection_pool import DatabaseConnectionPool

class ProductRepository:
    def __init__(self):
        self.connection_pool = DatabaseConnectionPool()

    def delete_product(self, product_id):
        conn = self.connection_pool.get_connection()
        try:
            with conn.cursor() as cursor:
                # Verificar si el producto existe
                cursor.execute("SELECT id FROM ProductsTable WHERE id = %s", (product_id,))
                if cursor.fetchone() is None:
                    raise ProductNotFoundException(f"Product with ID {product_id} not found")

                # Eliminar el producto
                query = sql.SQL("DELETE FROM ProductsTable WHERE id = %s")
                cursor.execute(query, (product_id,))
                conn.commit()
        finally:
            self.connection_pool.put_connection(conn)
