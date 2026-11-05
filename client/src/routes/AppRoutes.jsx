import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Login from "../pages/auth/Login";

import Dashboard from "../pages/dashboard/Dashboard";

import UserList from "../pages/users/UserList";
import UserForm from "../pages/users/UserForm";

import ClientList from "../pages/clients/ClientList";
import ClientForm from "../pages/clients/ClientForm";

import ProjectList from "../pages/projects/ProjectList";
import ProjectForm from "../pages/projects/ProjectForm";

import RoleList from "../pages/roles/RoleList";

import AllocationList from "../pages/allocations/AllocationList";

import TaskList from "../pages/tasks/TaskList";
import TaskForm from "../pages/tasks/TaskForm";

import TimesheetList from "../pages/timesheets/TimesheetList";
import TimesheetForm from "../pages/timesheets/TimesheetForm";
import ApprovalQueue from "../pages/timesheets/ApprovalQueue";

import MainLayout from "../layouts/MainLayout";

export default function AppRoutes() {

  return (
    <BrowserRouter>

      <Routes>

        {/* Login */}

        <Route
          path="/"
          element={<Login />}
        />

        {/* Main Layout */}

        <Route element={<MainLayout />}>

          {/* Dashboard */}

          <Route
            path="/dashboard"
            element={<Dashboard />}
          />

          {/* Roles */}

          <Route
            path="/roles"
            element={<RoleList />}
          />

          {/* Users */}

          <Route
            path="/users"
            element={<UserList />}
          />

          <Route
            path="/users/create"
            element={<UserForm />}
          />

          <Route
            path="/users/edit/:id"
            element={<UserForm />}
          />

          {/* Clients */}

          <Route
            path="/clients"
            element={<ClientList />}
          />

          <Route
            path="/clients/create"
            element={<ClientForm />}
          />

          <Route
            path="/clients/edit/:id"
            element={<ClientForm />}
          />

          {/* Projects */}

          <Route
            path="/projects"
            element={<ProjectList />}
          />

          <Route
            path="/projects/create"
            element={<ProjectForm />}
          />

          <Route
            path="/projects/edit/:id"
            element={<ProjectForm />}
          />

          {/* Allocations */}

          <Route
            path="/allocations"
            element={<AllocationList />}
          />

          {/* Tasks */}

          <Route
            path="/tasks"
            element={<TaskList />}
          />

          <Route
            path="/tasks/create"
            element={<TaskForm />}
          />

          <Route
            path="/tasks/edit/:id"
            element={<TaskForm />}
          />

          {/* Timesheets */}

          <Route
            path="/timesheets"
            element={<TimesheetList />}
          />

          <Route
            path="/timesheets/create"
            element={<TimesheetForm />}
          />

          <Route
            path="/timesheets/edit/:id"
            element={<TimesheetForm />}
          />

          <Route
            path="/timesheets/approvals"
            element={<ApprovalQueue />}
          />

        </Route>

      </Routes>

    </BrowserRouter>
  );
}