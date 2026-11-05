from sqlalchemy import select
from sqlalchemy import delete

from models.model import Role


class RoleService:

    def __init__(self, db):
        self.db = db

    async def create_role(
        self,
        payload
    ):

        result = await self.db.execute(
            select(Role).where(
                Role.role_name == payload.role_name
            )
        )

        existing_role = result.scalar_one_or_none()

        if existing_role:
            raise Exception(
                "Role already exists"
            )

        role = Role(
            role_name=payload.role_name.upper()
        )

        self.db.add(role)

        await self.db.commit()

        await self.db.refresh(role)

        return role

    async def get_roles(self):

        result = await self.db.execute(
            select(Role)
        )

        return result.scalars().all()

    async def get_role(
        self,
        role_id
    ):

        result = await self.db.execute(
            select(Role).where(
                Role.id == role_id
            )
        )

        return result.scalar_one_or_none()

    async def update_role(
        self,
        role,
        payload
    ):

        role.role_name = (
            payload.role_name.upper()
        )

        await self.db.commit()

        await self.db.refresh(role)

        return role

    async def delete_role(
        self,
        role_id
    ):


        result = await self.db.execute(
                   select(Role).where(
                       Role.id == role_id
                   )
               )

        role = result.scalar_one_or_none()

        if not role:
            raise Exception("Role not found")


        role.is_deleted = True

        await self.db.commit()

    async def seed_roles(self):

        default_roles = [
            "SUPER_ADMIN",
            "MANAGER",
            "EMPLOYEE"
        ]

        for role_name in default_roles:

            result = await self.db.execute(
                select(Role).where(
                    Role.role_name == role_name
                )
            )

            role = result.scalar_one_or_none()

            if not role:

                role = Role(
                    role_name=role_name
                )

                self.db.add(role)

        await self.db.commit()

        return {
            "message": "Roles seeded successfully"
        }