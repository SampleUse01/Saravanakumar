from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from core.config import settings


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    password = password.strip()

    if len(password) < 8:
        raise ValueError(
            "Password must contain at least 8 characters"
        )

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(data: dict) -> str:

    payload = data.copy()

    payload.update(
        {
            "exp": datetime.now(timezone.utc)
            + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        }
    )

    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=ALGORITHM
    )


def create_refresh_token(data: dict) -> str:

    payload = data.copy()

    payload.update(
        {
            "exp": datetime.now(timezone.utc)
            + timedelta(
                days=settings.REFRESH_TOKEN_EXPIRE_DAYS
            )
        }
    )

    return jwt.encode(
        payload,
        settings.JWT_REFRESH_SECRET,
        algorithm=ALGORITHM
    )