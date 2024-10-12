from psycopg2 import sql
from common.exceptions import DatabaseError
from database.connection_pool import DatabaseConnectionPool

class UserRepository:
    def __init__(self):
        self.connection_pool = DatabaseConnectionPool()

    def get_user_by_username(self, username):
        conn = self.connection_pool.get_connection()
        try:
            with conn.cursor() as cursor:
                query = sql.SQL("SELECT * FROM UsersTable WHERE username = %s")
                cursor.execute(query, (username,))
                user = cursor.fetchone()
                if not user:
                    return None
                return {
                    'id': user[0],
                    'username': user[1],
                    'password': user[2]
                }
        except Exception as e:
            raise DatabaseError(f"An error occurred fetching user: {str(e)}")
        finally:
            self.connection_pool.put_connection(conn)
