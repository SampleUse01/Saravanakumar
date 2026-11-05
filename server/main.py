from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from sqlalchemy import text
from models.model import Base
from core.config import settings

from controllers.auth_controller import router as auth_router
from controllers.user_controller import router as user_router
from controllers.client_controller import router as client_router
from controllers.project_controller import router as project_router
from controllers.task_controller import router as task_router   
from controllers.timesheet_controller import router as timesheet_router
from controllers.allocation_controller import (
    router as allocation_router
)

from controllers.dashboard_controller import (
    router as dashboard_router
)

from controllers.report_controller import (
    router as report_router
)

from controllers.role_controller import router as role_controller




import uvicorn
from database.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):

    try:
        # Check PostgreSQL Connection
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))

        print("=" * 50)
        print("✅ PostgreSQL Connected Successfully")
        print("=" * 50)

        # Create Tables
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        print("=" * 50)
        print("✅ All Tables Created Successfully")
        print("=" * 50)

    except Exception as ex:
        print("=" * 50)
        print("❌ Application Startup Failed")
        print(f"ERROR: {ex}")
        print("=" * 50)

    yield

    print("=" * 50)
    print("🛑 Application Shutdown")
    print("=" * 50)


app = FastAPI(
    title="Project Timeline Management System",
    version="1.0.0",
    default_response_class=ORJSONResponse,
    lifespan=lifespan
)

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(client_router)
app.include_router(project_router)
app.include_router(task_router)
app.include_router(timesheet_router)
app.include_router(allocation_router)
app.include_router(dashboard_router)
app.include_router(report_router)
app.include_router(role_controller)
@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )