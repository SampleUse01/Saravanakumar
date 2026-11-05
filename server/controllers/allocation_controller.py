from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db

from schemas.allocation_schema import (
    AllocationCreate,
    AllocationUpdate
)

from services.allocation_service import (
    AllocationService
)


router = APIRouter(
    prefix="/api/v1/allocations",
    tags=["Allocations"]
)

@router.post("/")
async def create_allocation(
    payload: AllocationCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = AllocationService(db)

        allocation = await service.create_allocation(
            payload
        )

        return {
            "success": True,
            "message": "Allocation created successfully",
            "data": allocation
        }

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


@router.get("/")
async def get_allocations(
    db: AsyncSession = Depends(get_db)
):

    service = AllocationService(db)

    return await service.get_allocations()


@router.get("/{allocation_id}")
async def get_allocation(
    allocation_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = AllocationService(db)

    allocation = await service.get_allocation(
        allocation_id
    )

    if not allocation:
        raise HTTPException(
            status_code=404,
            detail="Allocation not found"
        )

    return allocation

@router.put("/{allocation_id}")
async def update_allocation(
    allocation_id: UUID,
    payload: AllocationUpdate,
    db: AsyncSession = Depends(get_db)
):

    service = AllocationService(db)

    allocation = await service.get_allocation(
        allocation_id
    )

    if not allocation:
        raise HTTPException(
            status_code=404,
            detail="Allocation not found"
        )

    return await service.update_allocation(
        allocation,
        payload
    )

@router.put("/{allocation_id}")
async def update_allocation(
    allocation_id: UUID,
    payload: AllocationUpdate,
    db: AsyncSession = Depends(get_db)
):

    service = AllocationService(db)

    allocation = await service.get_allocation(
        allocation_id
    )

    if not allocation:
        raise HTTPException(
            status_code=404,
            detail="Allocation not found"
        )

    return await service.update_allocation(
        allocation,
        payload
    )


@router.get("/user/{user_id}")
async def get_user_allocations(
    user_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = AllocationService(db)

    return await service.get_user_allocations(
        user_id
    )


@router.get("/project/{project_id}")
async def get_project_allocations(
    project_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = AllocationService(db)

    return await service.get_project_allocations(
        project_id
    )



@router.get("/user/{user_id}/utilization")
async def get_utilization(
    user_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = AllocationService(db)

    return await service.calculate_utilization(
        user_id
    )


