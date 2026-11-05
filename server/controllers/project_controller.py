from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db

from schemas.project_schema import (
    ProjectCreate,
    ProjectUpdate
)

from services.project_service import (
    ProjectService
)

router = APIRouter(
    prefix="/api/v1/projects",
    tags=["Projects"]
)
@router.post("/")
async def create_project(
    payload: ProjectCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = ProjectService(db)

        project = await service.create_project(
            payload
        )

        return {
            "success": True,
            "message": "Project created successfully",
            "data": project
        }

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

@router.post("/")
async def create_project(
    payload: ProjectCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = ProjectService(db)

        project = await service.create_project(
            payload
        )

        return {
            "success": True,
            "message": "Project created successfully",
            "data": project
        }

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


@router.post("/")
async def create_project(
    payload: ProjectCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = ProjectService(db)

        project = await service.create_project(
            payload
        )

        return {
            "success": True,
            "message": "Project created successfully",
            "data": project
        }

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

@router.post("/")
async def create_project(
    payload: ProjectCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = ProjectService(db)

        project = await service.create_project(
            payload
        )

        return {
            "success": True,
            "message": "Project created successfully",
            "data": project
        }

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

@router.delete("/{project_id}")
async def delete_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = ProjectService(db)

    await service.delete_project(
        project_id
    )

    return {
        "success": True,
        "message": "Project deleted successfully"
    }


@router.delete("/{project_id}")
async def delete_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = ProjectService(db)

    await service.delete_project(
        project_id
    )

    return {
        "success": True,
        "message": "Project deleted successfully"
    }

@router.get("/status/{status}")
async def get_projects_by_status(
    status: str,
    db: AsyncSession = Depends(get_db)
):

    service = ProjectService(db)

    projects = await service.get_projects_by_status(
        status
    )

    return {
        "success": True,
        "data": projects
    }


