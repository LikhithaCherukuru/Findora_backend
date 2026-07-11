from fastapi import HTTPException


def verify_token(token: str):
    """
    JWT verification will be implemented in Phase 1.2.3
    """
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized",
        )