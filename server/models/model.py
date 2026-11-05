# models/model.py

import uuid
from datetime import date, datetime

from sqlalchemy import (
    String,
    Text,
    Boolean,
    Date,
    DateTime,
    Numeric,
    ForeignKey,
    func
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)


# =====================================================
# Base
# =====================================================

class Base(DeclarativeBase):
    pass


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )


# =====================================================
# Roles
# =====================================================

class Role(BaseModel):
    __tablename__ = "roles"

    role_name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    is_deleted :Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )


# =====================================================
# Users
# =====================================================

class User(BaseModel):
    __tablename__ = "users"

    employee_code: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
        nullable=True
    )

    first_name: Mapped[str] = mapped_column(
        String(100)
    )

    last_name: Mapped[str] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(500)
    )

    role_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("roles.id")
    )

    manager_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    designation: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    department: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    joining_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVE"
    )


# =====================================================
# Refresh Tokens
# =====================================================

class RefreshToken(BaseModel):
    __tablename__ = "refresh_tokens"

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )

    token: Mapped[str] = mapped_column(
        Text
    )

    revoked: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True)
    )


# =====================================================
# Clients
# =====================================================

class Client(BaseModel):
    __tablename__ = "clients"

    client_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    contact_person: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    address: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVE"
    )

    created_by: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )


# =====================================================
# Projects
# =====================================================

class Project(BaseModel):
    __tablename__ = "projects"

    client_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("clients.id")
    )

    project_code: Mapped[str] = mapped_column(
        String(50),
        unique=True
    )

    project_name: Mapped[str] = mapped_column(
        String(255)
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    start_date: Mapped[date] = mapped_column(Date)

    end_date: Mapped[date] = mapped_column(Date)

    budget: Mapped[float | None] = mapped_column(
        Numeric(15, 2),
        nullable=True
    )

    planned_hours: Mapped[float | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50)
    )


# =====================================================
# Project Allocations
# =====================================================

class ProjectAllocation(BaseModel):
    __tablename__ = "project_allocations"

    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id")
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )

    allocation_percentage: Mapped[float] = mapped_column(
        Numeric(5, 2)
    )

    allocated_from: Mapped[date] = mapped_column(Date)

    allocated_to: Mapped[date] = mapped_column(Date)

    allocated_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )


# =====================================================
# Milestones
# =====================================================

class Milestone(BaseModel):
    __tablename__ = "milestones"

    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id")
    )

    milestone_name: Mapped[str] = mapped_column(
        String(255)
    )

    planned_start: Mapped[date] = mapped_column(Date)

    planned_end: Mapped[date] = mapped_column(Date)

    actual_start: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    actual_end: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50)
    )


# =====================================================
# Tasks
# =====================================================

class Task(BaseModel):
    __tablename__ = "tasks"

    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id")
    )

    milestone_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("milestones.id"),
        nullable=True
    )

    task_name: Mapped[str] = mapped_column(
        String(255)
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    priority: Mapped[str] = mapped_column(
        String(20)
    )

    planned_hours: Mapped[float] = mapped_column(
        Numeric(8, 2)
    )

    start_date: Mapped[date] = mapped_column(Date)

    due_date: Mapped[date] = mapped_column(Date)

    status: Mapped[str] = mapped_column(
        String(50)
    )

    assigned_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )


# =====================================================
# Task Assignments
# =====================================================

class TaskAssignment(BaseModel):
    __tablename__ = "task_assignments"

    task_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tasks.id")
    )

    employee_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )

    allocation_percentage: Mapped[float] = mapped_column(
        Numeric(5, 2)
    )


# =====================================================
# Activity Types
# =====================================================

class ActivityType(BaseModel):
    __tablename__ = "activity_types"

    activity_name: Mapped[str] = mapped_column(
        String(100)
    )


# =====================================================
# Timesheets
# =====================================================

# =====================================================
# Timesheets
# =====================================================

class Timesheet(BaseModel):
    __tablename__ = "timesheets"

    employee_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )

    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id")
    )

    task_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("tasks.id"),
        nullable=True
    )

    work_date: Mapped[date] = mapped_column(
        Date
    )

    total_hours: Mapped[float] = mapped_column(
        Numeric(5, 2)
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    billable: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    activity_type_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("activity_types.id")
    )

    # ==========================================
    # Approval Workflow
    # ==========================================

    timesheet_status: Mapped[str] = mapped_column(
        String(20),
        default="DRAFT"
    )

    submitted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    approved_by: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    approved_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    rejected_by: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    rejected_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    rejection_reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

# =====================================================
# Meetings
# =====================================================

class Meeting(BaseModel):
    __tablename__ = "meetings"

    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id")
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    meeting_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True)
    )

    duration_hours: Mapped[float] = mapped_column(
        Numeric(5, 2)
    )

    organizer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )