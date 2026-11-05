from sqlalchemy import select, delete

from passlib.context import CryptContext

from models.model import User

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class UserService:

    def __init__(self, db):
        self.db = db

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    async def create_user(self, payload):

        # check email already exists
        result = await self.db.execute(
            select(User).where(
                User.email == payload.email
            )
        )

        existing_user = result.scalar_one_or_none()

        if existing_user:
            raise Exception(
                "Email already exists"
            )

        hashed_password = self.hash_password(
            payload.password
        )

        user = User(
            employee_code=payload.employee_code,
            first_name=payload.first_name,
            last_name=payload.last_name,
            email=payload.email,
            password_hash=hashed_password,
            role_id=payload.role_id,
            manager_id=payload.manager_id,
            designation=payload.designation,
            department=payload.department,
            joining_date=payload.joining_date,
        )

        self.db.add(user)

        await self.db.commit()

        await self.db.refresh(user)

        return user

    async def get_users(self):

        result = await self.db.execute(
            select(User)
        )

        return result.scalars().all()

    async def get_user(self, user_id):

        result = await self.db.execute(
            select(User).where(
                User.id == user_id
            )
        )

        return result.scalar_one_or_none()

    async def update_user(
        self,
        user,
        payload
    ):

        data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(
                user,
                key,
                value
            )

        await self.db.commit()

        await self.db.refresh(user)

        return user

    async def delete_user(self, user_id):

        await self.db.execute(
            delete(User).where(
                User.id == user_id
            )
        )

        await self.db.commit()
