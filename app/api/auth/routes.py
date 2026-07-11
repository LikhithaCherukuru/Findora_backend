from fastapi import APIRouter, HTTPException

from app.schemas.auth.register_schema import RegisterRequest
from app.schemas.auth.login_schema import LoginRequest

from app.services.auth.auth_service import AuthService

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)

service = AuthService()


@router.post("/register")
def register(request: RegisterRequest):

    try:

        response = service.register(
            request.full_name,
            request.email,
            request.password,
        )

        return {
            "success": True,
            "message": "Registration successful.",
            "user": response.user,
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post("/login")
def login(request: LoginRequest):

    try:

        response = service.login(
            request.email,
            request.password,
        )

        return {
            "success": True,
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token,
            "user": response.user,
        }

    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail=str(e),
        )