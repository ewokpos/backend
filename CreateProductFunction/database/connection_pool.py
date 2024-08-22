import os
import psycopg2
from psycopg2.pool import SimpleConnectionPool
from common.config import load_config

class DatabaseConnectionPool:
    def __init__(self):
        self.pool = None
        self.initialize_pool()

    def initialize_pool(self):
        config = load_config()
        dsn = config.get('DATABASE_URL')
        root_cert_path = config.get('ROOT_CERT_PATH')

        self.pool = SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dsn=dsn,
            sslmode='verify-full',
            sslrootcert=root_cert_path,
            application_name="docs_lambda_python"
        )
    
    def get_connection(self):
        return self.pool.getconn()

    def put_connection(self, conn):
        self.pool.putconn(conn)