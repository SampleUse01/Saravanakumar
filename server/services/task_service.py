from sqlalchemy import select, delete

from models.model import (
    Task,
    Project
)


class TaskService:

    def __init__(self, db):
        self.db = db

    async def create_task(self, payload):

        result = await self.db.execute(
            select(Project).where(
                Project.id == payload.project_id
            )
        )

        project = result.scalar_one_or_none()

        if not project:
            raise Exception(
                "Project not found"
            )

        task = Task(
            project_id=payload.project_id,
            milestone_id=payload.milestone_id,
            task_name=payload.task_name,
            description=payload.description,
            priority=payload.priority,
            planned_hours=payload.planned_hours,
            start_date=payload.start_date,
            due_date=payload.due_date,
            status=payload.status,
            assigned_by=payload.assigned_by
        )

        self.db.add(task)

        await self.db.commit()

        await self.db.refresh(task)

        return task

    async def get_tasks(self):

        result = await self.db.execute(
            select(Task)
        )

        return result.scalars().all()

    async def get_task(self, task_id):

        result = await self.db.execute(
            select(Task).where(
                Task.id == task_id
            )
        )

        return result.scalar_one_or_none()

    async def update_task(self, task, payload):

        data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(task, key, value)

        await self.db.commit()
        await self.db.refresh(task)

        return task

    async def delete_task(self, task_id):

        await self.db.execute(
            delete(Task).where(
                Task.id == task_id
            )
        )

        await self.db.commit()

    async def get_tasks_by_project(
        self,
        project_id
    ):

        result = await self.db.execute(
            select(Task).where(
                Task.project_id == project_id
            )
        )

        return result.scalars().all()

    async def get_tasks_by_status(
        self,
        status
    ):

        result = await self.db.execute(
            select(Task).where(
                Task.status == status
            )
        )

        return result.scalars().all()

    async def update_task_status(
        self,
        task,
        status
    ):

        task.status = status

        await self.db.commit()
        await self.db.refresh(task)

        return task

    async def update_task_priority(
        self,
        task,
        priority
    ):

        task.priority = priority

        await self.db.commit()
        await self.db.refresh(task)

        return task