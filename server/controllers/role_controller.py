from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db

from schemas.role_schema import (
    RoleCreate,
    RoleUpdate
)

from services.role_service import (
    RoleService
)

router = APIRouter(
    prefix="/api/v1/roles",
    tags=["Roles"]
)


@router.post("/")
async def create_role(
    payload: RoleCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = RoleService(db)

        role = await service.create_role(
            payload
        )

        return {
            "success": True,
            "message": "Role created successfully",
            "data": role
        }

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

@router.get("/")
async def get_roles(
    db: AsyncSession = Depends(get_db)
):

    service = RoleService(db)

    roles = await service.get_roles()

    return {
        "success": True,
        "data": roles
    }


@router.get("/{role_id}")
async def get_role(
    role_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = RoleService(db)

    role = await service.get_role(
        role_id
    )

    if not role:

        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return {
        "success": True,
        "data": role
    }


@router.put("/{role_id}")
async def update_role(
    role_id: UUID,
    payload: RoleUpdate,
    db: AsyncSession = Depends(get_db)
):

    service = RoleService(db)

    role = await service.get_role(
        role_id
    )

    if not role:

        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    updated = await service.update_role(
        role,
        payload
    )

    return {
        "success": True,
        "message": "Role updated successfully",
        "data": updated
    }


@router.delete("/{role_id}")
async def delete_role(
    role_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = RoleService(db)

    await service.delete_role(
        role_id
    )

    return {
        "success": True,
        "message": "Role deleted successfully"
    }

@router.post("/seed/default")
async def seed_roles(
    db: AsyncSession = Depends(get_db)
):

    service = RoleService(db)

    return await service.seed_roles()


