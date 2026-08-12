from fastapi import Depends, HTTPException, status

from app.auth.oauth2 import get_current_user


def require_admin(current_user=Depends(get_current_user)):
    """
    Allow only Admin users.
    """

    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Admin can perform this action."
        )

    return current_user


def require_student(current_user=Depends(get_current_user)):
    """
    Allow only Student users.
    """

    if current_user["role"] != "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Students can perform this action."
        )

    return current_user