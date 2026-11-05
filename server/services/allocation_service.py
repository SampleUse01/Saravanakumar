from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy import func

from models.model import (
    ProjectAllocation,
    User,
    Project
)


class AllocationService:

    def __init__(self, db):
        self.db = db

    async def validate_allocation(
        self,
        user_id,
        allocation_percentage
    ):

        result = await self.db.execute(
            select(
                func.coalesce(
                    func.sum(
                        ProjectAllocation.allocation_percentage
                    ),
                    0
                )
            ).where(
                ProjectAllocation.user_id == user_id
            )
        )

        current_allocation = result.scalar()

        total = (
            float(current_allocation)
            + float(allocation_percentage)
        )

        if total > 100:
            raise Exception(
                f"Allocation exceeded. Current={current_allocation}% Requested={allocation_percentage}%"
            )

    async def create_allocation(
        self,
        payload
    ):

        project_result = await self.db.execute(
            select(Project).where(
                Project.id == payload.project_id
            )
        )

        project = project_result.scalar_one_or_none()

        if not project:
            raise Exception(
                "Project not found"
            )

        user_result = await self.db.execute(
            select(User).where(
                User.id == payload.user_id
            )
        )

        user = user_result.scalar_one_or_none()

        if not user:
            raise Exception(
                "User not found"
            )

        await self.validate_allocation(
            payload.user_id,
            payload.allocation_percentage
        )

        allocation = ProjectAllocation(
            project_id=payload.project_id,
            user_id=payload.user_id,
            allocation_percentage=payload.allocation_percentage,
            allocated_from=payload.allocated_from,
            allocated_to=payload.allocated_to,
            allocated_by=payload.allocated_by
        )

        self.db.add(allocation)

        await self.db.commit()

        await self.db.refresh(allocation)

        return allocation

    async def get_allocations(self):

        result = await self.db.execute(
            select(ProjectAllocation)
        )

        return result.scalars().all()

    async def get_allocation(
        self,
        allocation_id
    ):

        result = await self.db.execute(
            select(ProjectAllocation).where(
                ProjectAllocation.id == allocation_id
            )
        )

        return result.scalar_one_or_none()

    async def update_allocation(
        self,
        allocation,
        payload
    ):

        data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(
                allocation,
                key,
                value
            )

        await self.db.commit()

        await self.db.refresh(allocation)

        return allocation

    async def delete_allocation(
        self,
        allocation_id
    ):

        await self.db.execute(
            delete(ProjectAllocation).where(
                ProjectAllocation.id == allocation_id
            )
        )

        await self.db.commit()

    async def get_user_allocations(
        self,
        user_id
    ):

        result = await self.db.execute(
            select(ProjectAllocation).where(
                ProjectAllocation.user_id == user_id
            )
        )

        return result.scalars().all()

    async def get_project_allocations(
        self,
        project_id
    ):

        result = await self.db.execute(
            select(ProjectAllocation).where(
                ProjectAllocation.project_id
                == project_id
            )
        )

        return result.scalars().all()

    async def calculate_utilization(
        self,
        user_id
    ):

        result = await self.db.execute(
            select(
                func.coalesce(
                    func.sum(
                        ProjectAllocation.allocation_percentage
                    ),
                    0
                )
            ).where(
                ProjectAllocation.user_id == user_id
            )
        )

        allocation = float(result.scalar())

        available = 100 - allocation

        if allocation < 75:
            status = "UNDER_UTILIZED"

        elif allocation <= 100:
            status = "OPTIMAL"

        else:
            status = "OVER_UTILIZED"

        return {
            "allocated_percentage": allocation,
            "available_percentage": available,
            "status": status
        }