import os
import psycopg2
from psycopg2.pool import SimpleConnectionPool
from common.config import load_config

pool = None

def initialize_pool():
    global pool
    if pool is None:
        config = load_config()
        dsn = config.get('DATABASE_URL')
        root_cert_path = config.get('ROOT_CERT_PATH')

        pool = SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dsn=dsn,
            sslmode='verify-full',
            sslrootcert=root_cert_path,
            application_name="docs_lambda_python"
        )

class DatabaseConnectionPool:
    def __init__(self):
        initialize_pool()

    def get_connection(self):
        try:
            conn = pool.getconn()
            if conn:
                print("Conexión obtenida exitosamente")
            return conn
        except Exception as e:
            print(f"Error obteniendo la conexión: {e}")
            raise e

    def put_connection(self, conn):
        try:
            pool.putconn(conn)
            print("Conexión devuelta al pool")
        except Exception as e:
            print(f"Error devolviendo la conexión: {e}")
            raise e
