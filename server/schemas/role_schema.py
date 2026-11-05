from uuid import UUID

from pydantic import BaseModel


class RoleCreate(BaseModel):
    role_name: str


class RoleUpdate(BaseModel):
    role_name: str


class RoleResponse(BaseModel):
    id: UUID
    role_name: str

    class Config:
        from_attributes = True