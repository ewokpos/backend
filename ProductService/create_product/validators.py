from pydantic import BaseModel, ValidationError, condecimal
from common.exceptions import BadRequestException

# Define el esquema para validar un producto
class ProductModel(BaseModel):
    name: str
    category: str
    price: condecimal(gt=0)  # Validar que el precio sea un número mayor que 0

def validate_product_data(data):
    try:
        # Intenta crear un objeto ProductModel con los datos de entrada
        product = ProductModel(**data)
        return product
    except ValidationError as e:
        # Si falla, lanza una excepción personalizada con los detalles del error
        raise BadRequestException(f"Validation Error: {e.errors()}")
