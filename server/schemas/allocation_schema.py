from uuid import UUID
from datetime import date

from pydantic import BaseModel, Field


class AllocationCreate(BaseModel):
    project_id: UUID
    user_id: UUID

    allocation_percentage: float = Field(
        gt=0,
        le=100
    )

    allocated_from: date
    allocated_to: date

    allocated_by: UUID


class AllocationUpdate(BaseModel):
    allocation_percentage: float | None = None
    allocated_from: date | None = None
    allocated_to: date | None = None


class AllocationResponse(BaseModel):
    id: UUID

    project_id: UUID

    user_id: UUID

    allocation_percentage: float

    class Config:
        from_attributes = True