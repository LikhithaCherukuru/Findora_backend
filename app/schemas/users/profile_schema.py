from pydantic import BaseModel


class UpdateProfileRequest(BaseModel):

    full_name: str

    avatar_url: str | None = None

    phone: str | None = None

    bio: str | None = None