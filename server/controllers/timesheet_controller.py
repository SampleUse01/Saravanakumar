from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db

from services.timesheet_service import TimesheetService

from schemas.timesheet_schema import (
    TimesheetCreate,
    TimesheetUpdate,
    RejectTimesheetRequest
)

router = APIRouter(
    prefix="/api/v1/timesheets",
    tags=["Timesheets"]
)


# =====================================================
# Create Timesheet
# =====================================================

@router.post("/")
async def create_timesheet(
    payload: TimesheetCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = TimesheetService(db)

        timesheet = await service.create_timesheet(
            payload
        )

        return {
            "success": True,
            "message": "Timesheet created successfully",
            "data": timesheet
        }

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


# =====================================================
# Get All Timesheets
# =====================================================

@router.get("/")
async def get_timesheets(
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    records = await service.get_timesheets()

    return {
        "success": True,
        "data": records
    }


# =====================================================
# Get Timesheet By Id
# =====================================================

@router.get("/{timesheet_id}")
async def get_timesheet(
    timesheet_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    timesheet = await service.get_timesheet(
        timesheet_id
    )

    if not timesheet:
        raise HTTPException(
            status_code=404,
            detail="Timesheet not found"
        )

    return {
        "success": True,
        "data": timesheet
    }


# =====================================================
# Update Timesheet
# =====================================================

@router.put("/{timesheet_id}")
async def update_timesheet(
    timesheet_id: UUID,
    payload: TimesheetUpdate,
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    timesheet = await service.get_timesheet(
        timesheet_id
    )

    if not timesheet:
        raise HTTPException(
            status_code=404,
            detail="Timesheet not found"
        )

    updated = await service.update_timesheet(
        timesheet,
        payload
    )

    return {
        "success": True,
        "message": "Timesheet updated successfully",
        "data": updated
    }


# =====================================================
# Delete Timesheet
# =====================================================

@router.delete("/{timesheet_id}")
async def delete_timesheet(
    timesheet_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    timesheet = await service.get_timesheet(
        timesheet_id
    )

    if not timesheet:
        raise HTTPException(
            status_code=404,
            detail="Timesheet not found"
        )

    await service.delete_timesheet(
        timesheet
    )

    return {
        "success": True,
        "message": "Timesheet deleted successfully"
    }


# =====================================================
# Submit Timesheet
# =====================================================

@router.post("/{timesheet_id}/submit")
async def submit_timesheet(
    timesheet_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    timesheet = await service.get_timesheet(
        timesheet_id
    )

    if not timesheet:
        raise HTTPException(
            status_code=404,
            detail="Timesheet not found"
        )

    submitted = await service.submit_timesheet(
        timesheet
    )

    return {
        "success": True,
        "message": "Timesheet submitted successfully",
        "data": submitted
    }


# =====================================================
# Approve Timesheet
# =====================================================

@router.post("/{timesheet_id}/approve")
async def approve_timesheet(
    timesheet_id: UUID,
    manager_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    timesheet = await service.get_timesheet(
        timesheet_id
    )

    if not timesheet:
        raise HTTPException(
            status_code=404,
            detail="Timesheet not found"
        )

    approved = await service.approve_timesheet(
        timesheet,
        manager_id
    )

    return {
        "success": True,
        "message": "Timesheet approved successfully",
        "data": approved
    }


# =====================================================
# Reject Timesheet
# =====================================================

@router.post("/{timesheet_id}/reject")
async def reject_timesheet(
    timesheet_id: UUID,
    manager_id: UUID,
    payload: RejectTimesheetRequest,
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    timesheet = await service.get_timesheet(
        timesheet_id
    )

    if not timesheet:
        raise HTTPException(
            status_code=404,
            detail="Timesheet not found"
        )

    rejected = await service.reject_timesheet(
        timesheet,
        manager_id,
        payload.reason
    )

    return {
        "success": True,
        "message": "Timesheet rejected successfully",
        "data": rejected
    }


# =====================================================
# Pending Approval Queue
# =====================================================

@router.get("/status/pending")
async def get_pending_timesheets(
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    return await service.get_pending_timesheets()


# =====================================================
# Approved Timesheets
# =====================================================

@router.get("/status/approved")
async def get_approved_timesheets(
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    return await service.get_approved_timesheets()


# =====================================================
# Rejected Timesheets
# =====================================================

@router.get("/status/rejected")
async def get_rejected_timesheets(
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    return await service.get_rejected_timesheets()


# =====================================================
# Employee Timesheets
# =====================================================

@router.get("/employee/{employee_id}")
async def get_employee_timesheets(
    employee_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    return await service.get_employee_timesheets(
        employee_id
    )


# =====================================================
# Project Timesheets
# =====================================================

@router.get("/project/{project_id}")
async def get_project_timesheets(
    project_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = TimesheetService(db)

    return await service.get_project_timesheets(
        project_id
    )