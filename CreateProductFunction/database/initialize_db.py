from database.connection_pool import DatabaseConnectionPool

def initialize_database():
    # Crear una instancia del pool de conexiones
    db_pool = DatabaseConnectionPool()
    
    # Obtener una conexión del pool
    conn = db_pool.get_connection()
    
    try:
        with conn.cursor() as cursor:
            # Leer el archivo SQL para crear la tabla
            with open('database_schema.sql', 'r') as f:
                schema_sql = f.read()

            # Ejecutar las sentencias SQL
            cursor.execute(schema_sql)
            conn.commit()
            print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing the database: {e}")
    finally:
        # Devolver la conexión al pool
        db_pool.put_connection(conn)

if __name__ == '__main__':
    initialize_database()
