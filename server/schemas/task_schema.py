from uuid import UUID
from datetime import date

from pydantic import BaseModel


class TaskCreate(BaseModel):
    project_id: UUID
    milestone_id: UUID | None = None

    task_name: str
    description: str | None = None

    priority: str = "MEDIUM"

    planned_hours: float

    start_date: date
    due_date: date

    status: str = "OPEN"

    assigned_by: UUID


class TaskUpdate(BaseModel):
    task_name: str | None = None
    description: str | None = None

    priority: str | None = None

    planned_hours: float | None = None

    start_date: date | None = None
    due_date: date | None = None

    status: str | None = None


class UpdateTaskStatus(BaseModel):
    status: str


class UpdateTaskPriority(BaseModel):
    priority: str