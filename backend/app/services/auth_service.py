from sqlalchemy.orm import Session

from app.database.user_model import UserDB
from app.models.user import UserRegister, UserLogin
from app.utils.security import hash_password, verify_password
from app.utils.jwt_handler import create_access_token


def register_user(db: Session, user: UserRegister):

    # Check if email already exists
    existing_user = db.query(UserDB).filter(
        UserDB.email == user.email
    ).first()

    if existing_user:
        return None

    # Hash the password
    hashed_password = hash_password(user.password)

    # Create new user
    new_user = UserDB(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, user: UserLogin):

    # Find user by email
    db_user = db.query(UserDB).filter(
        UserDB.email == user.email
    ).first()

    if db_user is None:
        return None

    # Verify password
    if not verify_password(user.password, db_user.password):
        return None

    # Generate JWT token with email and role
    access_token = create_access_token(
        data={
            "sub": db_user.email,
            "role": db_user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": db_user.role
    }