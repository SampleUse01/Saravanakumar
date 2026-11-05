from datetime import datetime

from jose import jwt
from sqlalchemy import select

from models.model import (
    User,
    RefreshToken
)

from core.config import settings

from core.security import (
    verify_password,
    create_access_token,
    create_refresh_token,
)

ALGORITHM = "HS256"


class AuthService:

    def __init__(self, db):
        self.db = db

    async def login(
        self,
        email,
        password
    ):

        result = await self.db.execute(
            select(User).where(
                User.email == email
            )
        )

        user = result.scalar_one_or_none()

        if not user:
            raise Exception(
                "Invalid email or password"
            )

        valid = verify_password(
            password,
            user.password_hash
        )

        if not valid:
            raise Exception(
                "Invalid email or password"
            )

        access_token = create_access_token({
            "sub": str(user.id),
            "email": user.email
        })

        refresh_token = create_refresh_token({
            "sub": str(user.id)
        })

        refresh_record = RefreshToken(
            user_id=user.id,
            token=refresh_token,
            expires_at=datetime.utcnow()
        )

        self.db.add(refresh_record)

        await self.db.commit()

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"
        }

    async def refresh_token(
        self,
        refresh_token: str
    ):

        payload = jwt.decode(
            refresh_token,
            settings.JWT_REFRESH_SECRET,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        result = await self.db.execute(
            select(User).where(
                User.id == user_id
            )
        )

        user = result.scalar_one_or_none()

        if not user:
            raise Exception("User not found")

        new_access_token = create_access_token({
            "sub": str(user.id),
            "email": user.email
        })

        return {
            "access_token": new_access_token
        }

    async def logout(
        self,
        refresh_token
    ):

        result = await self.db.execute(
            select(RefreshToken).where(
                RefreshToken.token == refresh_token
            )
        )

        token_obj = result.scalar_one_or_none()

        if token_obj:

            token_obj.revoked = True

            await self.db.commit()

        return {
            "message": "Logout successful"
        }