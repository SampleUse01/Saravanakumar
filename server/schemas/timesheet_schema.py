from uuid import UUID
from datetime import date

from pydantic import BaseModel


class TimesheetCreate(BaseModel):

    employee_id: UUID

    project_id: UUID

    task_id: UUID | None = None

    activity_type_id: UUID

    work_date: date

    total_hours: float

    remarks: str | None = None

    billable: bool = True


class TimesheetUpdate(BaseModel):

    total_hours: float | None = None

    remarks: str | None = None

    billable: bool | None = None


class RejectTimesheetRequest(BaseModel):

    reason: str