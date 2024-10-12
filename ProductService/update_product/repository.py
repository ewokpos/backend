from psycopg2 import sql
from common.exceptions import ProductNotFoundException, DatabaseError
from database.connection_pool import DatabaseConnectionPool
from database.models import Product

class ProductRepository:
    def __init__(self):
        self.connection_pool = DatabaseConnectionPool()

    def update_product(self, product_id, product_data):
        conn = self.connection_pool.get_connection()
        try:
            with conn.cursor() as cursor:
                # Verificar si el producto existe
                cursor.execute("SELECT id FROM ProductsTable WHERE id = %s", (product_id,))
                if cursor.fetchone() is None:
                    raise ProductNotFoundException(f"Product with ID {product_id} not found")

                # Actualizar el producto
                query = sql.SQL("""
                    UPDATE ProductsTable
                    SET name = %s, category = %s, price = %s, stock = %s, description = %s, sku = %s, barcode = %s, updated_at = current_timestamp
                    WHERE id = %s
                    RETURNING id;
                """)
                cursor.execute(query, (
                    product_data['name'],
                    product_data['category'],
                    product_data['price'],
                    product_data['stock'],
                    product_data['description'],
                    product_data['sku'],
                    product_data['barcode'],
                    product_id
                ))
                updated_product_id = cursor.fetchone()[0]
                conn.commit()
                
                return Product(
                    id=updated_product_id,
                    name=product_data['name'],
                    category=product_data['category'],
                    price=product_data['price'],
                    stock=product_data['stock'],
                    description=product_data['description'],
                    sku=product_data['sku'],
                    barcode=product_data['barcode']
                ).to_dict()
        finally:
            self.connection_pool.put_connection(conn)
