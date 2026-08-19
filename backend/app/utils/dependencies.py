from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.utils.jwt_handler import verify_access_token

security = HTTPBearer(auto_error=False)


def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    print("\n========== AUTH DEBUG ==========")
    print("Authorization Header:", request.headers.get("authorization"))
    print("Credentials:", credentials)

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    token = credentials.credentials

    user = verify_access_token(token)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return user


def get_current_student(
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "student":
        raise HTTPException(
            status_code=403,
            detail="Student access only"
        )

    return current_user


def get_current_mentor(
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "mentor":
        raise HTTPException(
            status_code=403,
            detail="Mentor access only"
        )

    return current_user


def get_current_admin(
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access only"
        )

    return current_user