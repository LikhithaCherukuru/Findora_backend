from app.repositories.users.user_repository import UserRepository


class UserService:

    def __init__(self):

        self.repository = UserRepository()

    def get_profile(
        self,
        user_id: str
    ):

        return self.repository.get_profile(
            user_id
        )

    def update_profile(
        self,
        user_id: str,
        data: dict
    ):

        return self.repository.update_profile(
            user_id,
            data
        )