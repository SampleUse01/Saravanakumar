from uuid import UUID
from pydantic import BaseModel, EmailStr


class ClientCreate(BaseModel):
    client_name: str
    contact_person: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    address: str | None = None
    status: str = "ACTIVE"
    created_by: UUID | None = None


class ClientUpdate(BaseModel):
    client_name: str | None = None
    contact_person: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    address: str | None = None
    status: str | None = None


class ClientResponse(BaseModel):
    id: UUID
    client_name: str
    contact_person: str | None
    email: str | None
    phone: str | None
    address: str | None
    status: str

    class Config:
        from_attributes = True