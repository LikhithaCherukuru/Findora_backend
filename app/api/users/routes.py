from fastapi import APIRouter, Depends

from app.middleware.auth import get_current_user

from app.schemas.users.profile_schema import (
    UpdateProfileRequest,
)

from app.services.users.user_service import (
    UserService,
)

router = APIRouter(

    prefix="/api/v1/users",

    tags=["Users"]

)

service = UserService()


@router.get("/me")
async def get_me(

    current_user=Depends(get_current_user)

):

    profile = service.get_profile(

        current_user.id

    )

    return profile.data


@router.patch("/me")
async def update_me(

    request: UpdateProfileRequest,

    current_user=Depends(get_current_user)

):

    profile = service.update_profile(

        current_user.id,

        request.model_dump()

    )

    return profile.data