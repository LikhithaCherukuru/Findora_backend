from app.core.database import supabase, supabase_admin


class AuthRepository:

    def register(
        self,
        email: str,
        password: str,
    ):

        return supabase.auth.sign_up(
            {
                "email": email,
                "password": password,
            }
        )

    def login(
        self,
        email: str,
        password: str,
    ):

        return supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password,
            }
        )

    def create_profile(
        self,
        user_id: str,
        full_name: str,
        email: str,
    ):

        return (
            supabase_admin
            .table("profiles")
            .insert(
                {
                    "id": user_id,
                    "full_name": full_name,
                }
            )
            .execute()
        )