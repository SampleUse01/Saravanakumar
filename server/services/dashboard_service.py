from sqlalchemy import select, func

from models.model import (
    Client,
    Project,
    User,
    Timesheet,
    Task
)


class DashboardService:

    def __init__(self, db):
        self.db = db

    async def ceo_dashboard(self):

        total_clients = await self.db.scalar(
            select(func.count(Client.id))
        )

        total_projects = await self.db.scalar(
            select(func.count(Project.id))
        )

        total_employees = await self.db.scalar(
            select(func.count(User.id))
        )

        active_projects = await self.db.scalar(
            select(func.count(Project.id))
            .where(Project.status == "IN_PROGRESS")
        )

        completed_projects = await self.db.scalar(
            select(func.count(Project.id))
            .where(Project.status == "COMPLETED")
        )

        billable_hours = await self.db.scalar(
            select(func.coalesce(func.sum(Timesheet.total_hours), 0))
            .where(Timesheet.billable == True)
        )

        non_billable_hours = await self.db.scalar(
            select(func.coalesce(func.sum(Timesheet.total_hours), 0))
            .where(Timesheet.billable == False)
        )

        return {
            "total_clients": total_clients,
            "total_projects": total_projects,
            "active_projects": active_projects,
            "completed_projects": completed_projects,
            "total_employees": total_employees,
            "billable_hours": float(billable_hours),
            "non_billable_hours": float(non_billable_hours)
        }

    async def manager_dashboard(self):

        pending_timesheets = await self.db.scalar(
            select(func.count(Timesheet.id))
            .where(Timesheet.timesheet_status == "SUBMITTED")
        )

        total_tasks = await self.db.scalar(
            select(func.count(Task.id))
        )

        completed_tasks = await self.db.scalar(
            select(func.count(Task.id))
            .where(Task.status == "COMPLETED")
        )

        return {
            "pending_timesheets": pending_timesheets,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks
        }

    async def employee_dashboard(
        self,
        employee_id
    ):

        my_timesheets = await self.db.scalar(
            select(func.count(Timesheet.id))
            .where(
                Timesheet.employee_id == employee_id
            )
        )

        approved_timesheets = await self.db.scalar(
            select(func.count(Timesheet.id))
            .where(
                Timesheet.employee_id == employee_id,
                Timesheet.timesheet_status == "APPROVED"
            )
        )

        return {
            "my_timesheets": my_timesheets,
            "approved_timesheets": approved_timesheets
        }