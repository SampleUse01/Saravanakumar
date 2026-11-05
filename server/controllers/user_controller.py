from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db

from schemas.user_schema import (
    UserCreate,
    UserUpdate
)

from services.user_service import UserService


router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)


@router.post("/")
async def create_user(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = UserService(db)

        user = await service.create_user(
            payload
        )

        return {
            "success": True,
            "message": "User created successfully",
            "data": user
        }

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


@router.get("/")
async def get_users(
    db: AsyncSession = Depends(get_db)
):

    service = UserService(db)

    users = await service.get_users()

    return {
        "success": True,
        "data": users
    }


@router.get("/{user_id}")
async def get_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = UserService(db)

    user = await service.get_user(
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "success": True,
        "data": user
    }


@router.put("/{user_id}")
async def update_user(
    user_id: UUID,
    payload: UserUpdate,
    db: AsyncSession = Depends(get_db)
):

    service = UserService(db)

    user = await service.get_user(
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    updated = await service.update_user(
        user,
        payload
    )

    return {
        "success": True,
        "message": "User updated successfully",
        "data": updated
    }


@router.delete("/{user_id}")
async def delete_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = UserService(db)

    await service.delete_user(
        user_id
    )

    return {
        "success": True,
        "message": "User deleted successfully"
    }