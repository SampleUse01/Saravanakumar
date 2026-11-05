from uuid import UUID
from datetime import date

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    client_id: UUID
    project_code: str
    project_name: str
    description: str | None = None

    start_date: date
    end_date: date

    budget: float | None = None
    planned_hours: float | None = None

    status: str = "NOT_STARTED"


class ProjectUpdate(BaseModel):
    project_name: str | None = None
    description: str | None = None

    start_date: date | None = None
    end_date: date | None = None

    budget: float | None = None
    planned_hours: float | None = None

    status: str | None = None