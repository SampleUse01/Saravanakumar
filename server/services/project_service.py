from sqlalchemy import select, delete

from models.model import (
    Project,
    Client
)


class ProjectService:

    def __init__(self, db):
        self.db = db

    async def create_project(self, payload):

        client_result = await self.db.execute(
            select(Client).where(
                Client.id == payload.client_id
            )
        )

        client = client_result.scalar_one_or_none()

        if not client:
            raise Exception(
                "Client not found"
            )

        project_result = await self.db.execute(
            select(Project).where(
                Project.project_code == payload.project_code
            )
        )

        existing_project = (
            project_result.scalar_one_or_none()
        )

        if existing_project:
            raise Exception(
                "Project code already exists"
            )

        project = Project(
            client_id=payload.client_id,
            project_code=payload.project_code,
            project_name=payload.project_name,
            description=payload.description,
            start_date=payload.start_date,
            end_date=payload.end_date,
            budget=payload.budget,
            planned_hours=payload.planned_hours,
            status=payload.status
        )

        self.db.add(project)

        await self.db.commit()

        await self.db.refresh(project)

        return project

    async def get_projects(self):

        result = await self.db.execute(
            select(Project)
        )

        return result.scalars().all()

    async def get_project(
        self,
        project_id
    ):

        result = await self.db.execute(
            select(Project).where(
                Project.id == project_id
            )
        )

        return result.scalar_one_or_none()

    async def update_project(
        self,
        project,
        payload
    ):

        data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():

            setattr(
                project,
                key,
                value
            )

        await self.db.commit()

        await self.db.refresh(project)

        return project

    async def delete_project(
        self,
        project_id
    ):

        await self.db.execute(
            delete(Project).where(
                Project.id == project_id
            )
        )

        await self.db.commit()

    async def get_projects_by_client(
        self,
        client_id
    ):

        result = await self.db.execute(
            select(Project).where(
                Project.client_id == client_id
            )
        )

        return result.scalars().all()

    async def get_projects_by_status(
        self,
        status
    ):

        result = await self.db.execute(
            select(Project).where(
                Project.status == status
            )
        )

        return result.scalars().all()