from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db

from schemas.task_schema import (
    TaskCreate,
    TaskUpdate,
    UpdateTaskStatus,
    UpdateTaskPriority
)

from services.task_service import (
    TaskService
)

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)


@router.post("/")
async def create_task(
    payload: TaskCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = TaskService(db)

        task = await service.create_task(
            payload
        )

        return {
            "success": True,
            "message": "Task created successfully",
            "data": task
        }

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

@router.get("/")
async def get_tasks(
    db: AsyncSession = Depends(get_db)
):

    service = TaskService(db)

    return await service.get_tasks()


@router.get("/{task_id}")
async def get_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = TaskService(db)

    task = await service.get_task(
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

@router.put("/{task_id}")
async def update_task(
    task_id: UUID,
    payload: TaskUpdate,
    db: AsyncSession = Depends(get_db)
):

    service = TaskService(db)

    task = await service.get_task(
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return await service.update_task(
        task,
        payload
    )


@router.delete("/{task_id}")
async def delete_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = TaskService(db)

    await service.delete_task(
        task_id
    )

    return {
        "success": True,
        "message": "Task deleted successfully"
    }


@router.get("/project/{project_id}")
async def get_tasks_by_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = TaskService(db)

    return await service.get_tasks_by_project(
        project_id
    )


@router.get("/status/{status}")
async def get_tasks_by_status(
    status: str,
    db: AsyncSession = Depends(get_db)
):

    service = TaskService(db)

    return await service.get_tasks_by_status(
        status
    )


@router.put("/{task_id}/status")
async def update_status(
    task_id: UUID,
    payload: UpdateTaskStatus,
    db: AsyncSession = Depends(get_db)
):

    service = TaskService(db)

    task = await service.get_task(
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return await service.update_task_status(
        task,
        payload.status
    )


@router.put("/{task_id}/priority")
async def update_priority(
    task_id: UUID,
    payload: UpdateTaskPriority,
    db: AsyncSession = Depends(get_db)
):

    service = TaskService(db)

    task = await service.get_task(
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return await service.update_task_priority(
        task,
        payload.priority
    )