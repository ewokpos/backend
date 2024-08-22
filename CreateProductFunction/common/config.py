import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

def load_config():
    """
    Carga la configuración de las variables de entorno.
    """
    return {
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'ROOT_CERT_PATH': os.getenv('ROOT_CERT_PATH', 'root.crt')  # Ruta por defecto si no está en el .env
    }
