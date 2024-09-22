from psycopg2 import sql
from common.exceptions import BadRequestException
from database.models import Product
from database.connection_pool import DatabaseConnectionPool

class ProductRepository:
    def __init__(self):
        self.connection_pool = DatabaseConnectionPool()

    def create_product(self, product_data):
        if not all(key in product_data for key in ('name', 'category', 'price', 'stock', 'description', 'sku', 'barcode')):
            raise BadRequestException("Missing required product fields")
        
        conn = self.connection_pool.get_connection()
        try:
            with conn.cursor() as cursor:
                query = sql.SQL("""
                    INSERT INTO ProductsTable (name, category, price, stock, description, sku, barcode)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING id;
                """)
                cursor.execute(query, (
                    product_data['name'],
                    product_data['category'],
                    product_data['price'],
                    product_data['stock'],
                    product_data['description'],
                    product_data['sku'],
                    product_data['barcode']
                ))
                product_id = cursor.fetchone()[0]
                conn.commit()
                return Product(
                    id=product_id,
                    name=product_data['name'],
                    category=product_data['category'],
                    price=product_data['price'],
                    stock=product_data['stock'],
                    description=product_data['description'],
                    sku=product_data['sku'],
                    barcode=product_data['barcode']
                ).to_dict()
        finally:
            self.connection_pool.put_connection(conn)  # Corregido para usar connection_pool
