from psycopg2 import sql
from database.connection_pool import DatabaseConnectionPool

class ReportRepository:
    def __init__(self):
        self.connection_pool = DatabaseConnectionPool()

    def generate_sales_report(self, query_params):
        conn = self.connection_pool.get_connection()
        try:
            with conn.cursor() as cursor:
                query = sql.SQL("SELECT * FROM SalesTable")  # Aquí podrías agregar filtros según query_params
                cursor.execute(query)
                sales = cursor.fetchall()
                return sales
        finally:
            self.connection_pool.put_connection(conn)
