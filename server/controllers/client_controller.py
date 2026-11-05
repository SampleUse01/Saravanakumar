from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db

from schemas.client_schema import (
    ClientCreate,
    ClientUpdate
)

from services.client_service import (
    ClientService
)

router = APIRouter(
    prefix="/api/v1/clients",
    tags=["Clients"]
)


@router.post("/")
async def create_client(
    payload: ClientCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = ClientService(db)

        client = await service.create_client(
            payload
        )

        return {
            "success": True,
            "message": "Client created successfully",
            "data": client
        }

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

@router.get("/")
async def get_clients(
    db: AsyncSession = Depends(get_db)
):

    service = ClientService(db)

    clients = await service.get_clients()

    return {
        "success": True,
        "data": clients
    }


@router.get("/{client_id}")
async def get_client(
    client_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = ClientService(db)

    client = await service.get_client(
        client_id
    )

    if not client:

        raise HTTPException(
            status_code=404,
            detail="Client not found"
        )

    return {
        "success": True,
        "data": client
    }


@router.put("/{client_id}")
async def update_client(
    client_id: UUID,
    payload: ClientUpdate,
    db: AsyncSession = Depends(get_db)
):

    service = ClientService(db)

    client = await service.get_client(
        client_id
    )

    if not client:

        raise HTTPException(
            status_code=404,
            detail="Client not found"
        )

    updated = await service.update_client(
        client,
        payload
    )

    return {
        "success": True,
        "message": "Client updated successfully",
        "data": updated
    }


@router.delete("/{client_id}")
async def delete_client(
    client_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    service = ClientService(db)

    await service.delete_client(
        client_id
    )

    return {
        "success": True,
        "message": "Client deleted successfully"
    }