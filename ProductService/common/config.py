import os
from dotenv import load_dotenv

# Verificar si estamos en un entorno local
if os.path.exists('.env'):
    load_dotenv()

def load_config():
    """
    Carga la configuración de las variables de entorno.
    En desarrollo carga desde .env, en producción desde el entorno de Lambda.
    """
    return {
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'ROOT_CERT_PATH': os.getenv('ROOT_CERT_PATH', 'root.crt')  # Ruta por defecto si no está en el .env
    }
