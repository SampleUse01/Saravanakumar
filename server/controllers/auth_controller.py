from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db

from schemas.auth_schema import (
    LoginRequest,
    RefreshRequest
)

from services.auth_service import (
    AuthService
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/login")
async def login(
    payload: LoginRequest,
    db: AsyncSession = Depends(get_db)
):

    try:

        service = AuthService(db)

        return await service.login(
            payload.email,
            payload.password
        )

    except Exception as ex:

        raise HTTPException(
            status_code=401,
            detail=str(ex)
        )


@router.post("/refresh")
async def refresh(
    payload: RefreshRequest,
    db: AsyncSession = Depends(get_db)
):

    service = AuthService(db)

    return await service.refresh_token(
        payload.refresh_token
    )



@router.post("/logout")
async def logout(
    payload: RefreshRequest,
    db: AsyncSession = Depends(get_db)
):

    service = AuthService(db)

    return await service.logout(
        payload.refresh_token
    )