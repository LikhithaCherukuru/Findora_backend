from app.repositories.auth.auth_repository import AuthRepository


class AuthService:

    def __init__(self):

        self.repository = AuthRepository()

    def register(
        self,
        full_name: str,
        email: str,
        password: str,
    ):

        auth_response = self.repository.register(
            email=email,
            password=password,
        )

        user = auth_response.user

        self.repository.create_profile(
            user.id,
            full_name,
            email,
        )

        return auth_response

    def login(
        self,
        email: str,
        password: str,
    ):

        return self.repository.login(
            email,
            password,
        )