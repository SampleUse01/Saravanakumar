from datetime import datetime

from sqlalchemy import select
from sqlalchemy import delete

from models.model import (
    Timesheet,
    Project,
    User,
    Task
)


class TimesheetService:

    def __init__(self, db):
        self.db = db

    async def create_timesheet(
        self,
        payload
    ):

        result = await self.db.execute(
            select(User).where(
                User.id == payload.employee_id
            )
        )

        employee = result.scalar_one_or_none()

        if not employee:
            raise Exception(
                "Employee not found"
            )

        timesheet = Timesheet(
            employee_id=payload.employee_id,
            project_id=payload.project_id,
            task_id=payload.task_id,
            activity_type_id=payload.activity_type_id,
            work_date=payload.work_date,
            total_hours=payload.total_hours,
            remarks=payload.remarks,
            billable=payload.billable,
            timesheet_status="DRAFT"
        )

        self.db.add(timesheet)

        await self.db.commit()

        await self.db.refresh(timesheet)

        return timesheet

    async def get_timesheets(self):

        result = await self.db.execute(
            select(Timesheet)
        )

        return result.scalars().all()

    async def get_timesheet(
        self,
        timesheet_id
    ):

        result = await self.db.execute(
            select(Timesheet).where(
                Timesheet.id == timesheet_id
            )
        )

        return result.scalar_one_or_none()

    async def update_timesheet(
        self,
        timesheet,
        payload
    ):

        if timesheet.timesheet_status != "DRAFT":
            raise Exception(
                "Only DRAFT timesheets can be updated"
            )

        data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(
                timesheet,
                key,
                value
            )

        await self.db.commit()

        await self.db.refresh(timesheet)

        return timesheet

    async def delete_timesheet(
        self,
        timesheet
    ):

        if timesheet.timesheet_status != "DRAFT":
            raise Exception(
                "Only DRAFT timesheets can be deleted"
            )

        await self.db.delete(timesheet)

        await self.db.commit()

    async def submit_timesheet(
        self,
        timesheet
    ):

        if timesheet.timesheet_status != "DRAFT":
            raise Exception(
                "Only DRAFT can be submitted"
            )

        timesheet.timesheet_status = "SUBMITTED"

        timesheet.submitted_at = datetime.utcnow()

        await self.db.commit()

        return timesheet

    async def approve_timesheet(
        self,
        timesheet,
        manager_id
    ):

        if timesheet.timesheet_status != "SUBMITTED":
            raise Exception(
                "Timesheet must be SUBMITTED"
            )

        timesheet.timesheet_status = "APPROVED"

        timesheet.approved_by = manager_id

        timesheet.approved_at = datetime.utcnow()

        await self.db.commit()

        return timesheet

    async def reject_timesheet(
        self,
        timesheet,
        manager_id,
        reason
    ):

        if timesheet.timesheet_status != "SUBMITTED":
            raise Exception(
                "Timesheet must be SUBMITTED"
            )

        timesheet.timesheet_status = "REJECTED"

        timesheet.rejected_by = manager_id

        timesheet.rejected_at = datetime.utcnow()

        timesheet.rejection_reason = reason

        await self.db.commit()

        return timesheet

    async def get_pending_timesheets(self):

        result = await self.db.execute(
            select(Timesheet).where(
                Timesheet.timesheet_status
                == "SUBMITTED"
            )
        )

        return result.scalars().all()

    async def get_approved_timesheets(self):

        result = await self.db.execute(
            select(Timesheet).where(
                Timesheet.timesheet_status
                == "APPROVED"
            )
        )

        return result.scalars().all()

    async def get_rejected_timesheets(self):

        result = await self.db.execute(
            select(Timesheet).where(
                Timesheet.timesheet_status
                == "REJECTED"
            )
        )

        return result.scalars().all()

    async def get_employee_timesheets(
        self,
        employee_id
    ):

        result = await self.db.execute(
            select(Timesheet).where(
                Timesheet.employee_id == employee_id
            )
        )

        return result.scalars().all()

    async def get_project_timesheets(
        self,
        project_id
    ):

        result = await self.db.execute(
            select(Timesheet).where(
                Timesheet.project_id == project_id
            )
        )

        return result.scalars().all()