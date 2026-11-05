from sqlalchemy import (
    select,
    func
)

from models.model import (
    Timesheet,
    Task,
    ProjectAllocation
)


class ReportService:

    def __init__(self, db):
        self.db = db

    async def billable_hours(self):

        total = await self.db.scalar(
            select(
                func.coalesce(
                    func.sum(
                        Timesheet.total_hours
                    ),
                    0
                )
            ).where(
                Timesheet.billable == True
            )
        )

        return {
            "billable_hours": float(total)
        }

    async def non_billable_hours(self):

        total = await self.db.scalar(
            select(
                func.coalesce(
                    func.sum(
                        Timesheet.total_hours
                    ),
                    0
                )
            ).where(
                Timesheet.billable == False
            )
        )

        return {
            "non_billable_hours": float(total)
        }

    async def project_progress(self):

        total_tasks = await self.db.scalar(
            select(func.count(Task.id))
        )

        completed_tasks = await self.db.scalar(
            select(func.count(Task.id))
            .where(
                Task.status == "COMPLETED"
            )
        )

        progress = 0

        if total_tasks:
            progress = (
                completed_tasks /
                total_tasks
            ) * 100

        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "progress_percentage": round(
                progress,
                2
            )
        }

    async def resource_allocation(self):

        total = await self.db.scalar(
            select(
                func.coalesce(
                    func.sum(
                        ProjectAllocation.allocation_percentage
                    ),
                    0
                )
            )
        )

        return {
            "total_allocated_percentage": float(total)
        }

    async def timesheet_compliance(self):

        approved = await self.db.scalar(
            select(
                func.count(
                    Timesheet.id
                )
            ).where(
                Timesheet.timesheet_status ==
                "APPROVED"
            )
        )

        submitted = await self.db.scalar(
            select(
                func.count(
                    Timesheet.id
                )
            )
        )

        compliance = 0

        if submitted:
            compliance = (
                approved /
                submitted
            ) * 100

        return {
            "approved": approved,
            "submitted": submitted,
            "compliance_percentage": round(
                compliance,
                2
            )
        }