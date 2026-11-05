from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db

from services.report_service import (
    ReportService
)

router = APIRouter(
    prefix="/api/v1/reports",
    tags=["Reports"]
)


@router.get("/billable")
async def billable_hours(
    db: AsyncSession = Depends(get_db)
):

    return await ReportService(
        db
    ).billable_hours()


@router.get("/non-billable")
async def non_billable_hours(
    db: AsyncSession = Depends(get_db)
):

    return await ReportService(
        db
    ).non_billable_hours()


@router.get("/project-progress")
async def project_progress(
    db: AsyncSession = Depends(get_db)
):

    return await ReportService(
        db
    ).project_progress()


@router.get("/resource-allocation")
async def resource_allocation(
    db: AsyncSession = Depends(get_db)
):

    return await ReportService(
        db
    ).resource_allocation()


@router.get("/timesheet-compliance")
async def timesheet_compliance(
    db: AsyncSession = Depends(get_db)
):

    return await ReportService(
        db
    ).timesheet_compliance()