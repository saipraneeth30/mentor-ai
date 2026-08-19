from datetime import datetime, timedelta
from jose import JWTError, jwt

from app.utils.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


def create_access_token(data: dict):
    """
    Create a JWT access token.
    """

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def verify_access_token(token: str):
    """
    Verify JWT token and return user information.
    """

    print("\n========== VERIFY TOKEN ==========")
    print("Received Token:")
    print(token)

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("\nDecoded Payload:")
        print(payload)

        email = payload.get("sub")
        role = payload.get("role")

        print("\nEmail:", email)
        print("Role:", role)

        if email is None or role is None:
            print("❌ Email or Role is missing inside JWT")
            return None

        print("✅ Token Verified Successfully")

        return {
            "email": email,
            "role": role
        }

    except JWTError as e:

        print("\n❌ JWT ERROR")
        print(type(e).__name__)
        print(str(e))

        return None

    except Exception as e:

        print("\n❌ UNKNOWN ERROR")
        print(type(e).__name__)
        print(str(e))

        return None