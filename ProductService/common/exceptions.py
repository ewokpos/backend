class BadRequestException(Exception):
    """Excepción para manejar errores relacionados con solicitudes incorrectas."""
    def __init__(self, message="Bad request"):
        super().__init__(message)

class DatabaseError(Exception):
    """Excepción general para errores de base de datos."""
    def __init__(self, message="Database error"):
        super().__init__(message)

class MissingFieldException(BadRequestException):
    """Excepción para manejar casos cuando faltan campos en los datos del producto."""
    def __init__(self, missing_fields):
        message = f"Missing required fields: {', '.join(missing_fields)}"
        super().__init__(message)

class InvalidDataException(BadRequestException):
    """Excepción para manejar casos de datos inválidos."""
    def __init__(self, message="Invalid data"):
        super().__init__(message)

class ProductNotFoundException(DatabaseError):
    """Excepción para manejar casos en los que no se encuentra el producto."""
    def __init__(self, message="Product not found"):
        super().__init__(message)
