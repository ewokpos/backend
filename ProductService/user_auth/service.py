from user_auth.repository import UserRepository
from common.exceptions import InvalidCredentialsException

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def authenticate_user(self, username, password):
        user = self.repository.get_user_by_username(username)
        
        if not user or not self._validate_password(user['password'], password):
            raise InvalidCredentialsException("Invalid username or password")
        
        # Generar token de autenticación (aquí podrías usar JWT o alguna otra técnica)
        token = self._generate_auth_token(user)
        
        return token

    def _validate_password(self, stored_password, provided_password):
        # Aquí agregarías la lógica para validar el password, por ejemplo con bcrypt
        return stored_password == provided_password

    def _generate_auth_token(self, user):
        # Genera un token para el usuario (podrías usar JWT aquí)
        return f"token_for_{user['username']}"
