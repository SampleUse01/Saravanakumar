from uuid import UUID
from datetime import date

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    employee_code: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    role_id: UUID

    manager_id: UUID | None = None
    designation: str | None = None
    department: str | None = None
    joining_date: date | None = None


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    designation: str | None = None
    department: str | None = None
    manager_id: UUID | None = None
    status: str | None = None