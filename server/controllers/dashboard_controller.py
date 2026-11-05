from uuid import UUID

from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db

from services.dashboard_service import (
    DashboardService
)

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"]
)


@router.get("/ceo")
async def ceo_dashboard(
    db: AsyncSession = Depends(get_db)
):

    return await DashboardService(
        db
    ).ceo_dashboard()


@router.get("/manager")
async def manager_dashboard(
    db: AsyncSession = Depends(get_db)
):

    return await DashboardService(
        db
    ).manager_dashboard()


@router.get("/employee/{employee_id}")
async def employee_dashboard(
    employee_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    return await DashboardService(
        db
    ).employee_dashboard(
        employee_id
    )