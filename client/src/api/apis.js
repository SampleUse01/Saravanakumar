import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    "Content-Type": "application/json"
  }
});
// ======================================================
// Auth APIs
// ======================================================

export const login = (data) =>
    api.post("/auth/login", data);

export const refreshToken = (data) =>
    api.post("/auth/refresh", data);

export const logout = (data) =>
    api.post("/auth/logout", data);

// ======================================================
// Roles APIs
// ======================================================

export const getRoles = () =>
    api.get("/roles");

export const getRoleById = (id) =>
    api.get(`/roles/${id}`);

export const createRole = (data) =>
    api.post("/roles", data);

export const updateRole = (id, data) =>
    api.put(`/roles/${id}`, data);

export const deleteRole = (id) =>
    api.delete(`/roles/${id}`);

export const seedRoles = () =>
    api.post("/roles/seed/default");

// ======================================================
// Users APIs
// ======================================================

export const getUsers = () =>
    api.get("/users");

export const getUserById = (id) =>
    api.get(`/users/${id}`);

export const createUser = (data) =>
    api.post("/users", data);

export const updateUser = (id, data) =>
    api.put(`/users/${id}`, data);

export const deleteUser = (id) =>
    api.delete(`/users/${id}`);

export const getManagers = () =>
    api.get("/users/managers");

export const getEmployees = () =>
    api.get("/users/employees");

// ======================================================
// Client APIs
// ======================================================

export const getClients = () =>
    api.get("/clients");

export const getClientById = (id) =>
    api.get(`/clients/${id}`);

export const createClient = (data) =>
    api.post("/clients", data);

export const updateClient = (id, data) =>
    api.put(`/clients/${id}`, data);

export const deleteClient = (id) =>
    api.delete(`/clients/${id}`);

// ======================================================
// Project APIs
// ======================================================

export const getProjects = () =>
    api.get("/projects");

export const getProjectById = (id) =>
    api.get(`/projects/${id}`);

export const createProject = (data) =>
    api.post("/projects", data);

export const updateProject = (id, data) =>
    api.put(`/projects/${id}`, data);

export const deleteProject = (id) =>
    api.delete(`/projects/${id}`);

export const getProjectsByClient = (clientId) =>
    api.get(`/projects/client/${clientId}`);

export const getProjectsByStatus = (status) =>
    api.get(`/projects/status/${status}`);

// ======================================================
// Allocation APIs
// ======================================================

export const getAllocations = () =>
    api.get("/allocations");

export const getAllocationById = (id) =>
    api.get(`/allocations/${id}`);

export const createAllocation = (data) =>
    api.post("/allocations", data);

export const updateAllocation = (id, data) =>
    api.put(`/allocations/${id}`, data);

export const deleteAllocation = (id) =>
    api.delete(`/allocations/${id}`);

export const getUserAllocations = (userId) =>
    api.get(`/allocations/user/${userId}`);

export const getProjectAllocations = (projectId) =>
    api.get(`/allocations/project/${projectId}`);

export const getResourceUtilization = (userId) =>
    api.get(`/allocations/user/${userId}/utilization`);

// ======================================================
// Task APIs
// ======================================================

export const getTasks = () =>
    api.get("/tasks");

export const getTaskById = (id) =>
    api.get(`/tasks/${id}`);

export const createTask = (data) =>
    api.post("/tasks", data);

export const updateTask = (id, data) =>
    api.put(`/tasks/${id}`, data);

export const deleteTask = (id) =>
    api.delete(`/tasks/${id}`);

export const getTasksByProject = (projectId) =>
    api.get(`/tasks/project/${projectId}`);

export const getTasksByStatus = (status) =>
    api.get(`/tasks/status/${status}`);

export const updateTaskStatus = (id, data) =>
    api.put(`/tasks/${id}/status`, data);

export const updateTaskPriority = (id, data) =>
    api.put(`/tasks/${id}/priority`, data);

// ======================================================
// Timesheet APIs
// ======================================================

export const getTimesheets = () =>
    api.get("/timesheets");

export const getTimesheetById = (id) =>
    api.get(`/timesheets/${id}`);

export const createTimesheet = (data) =>
    api.post("/timesheets", data);

export const updateTimesheet = (id, data) =>
    api.put(`/timesheets/${id}`, data);

export const deleteTimesheet = (id) =>
    api.delete(`/timesheets/${id}`);

export const submitTimesheet = (id) =>
    api.post(`/timesheets/${id}/submit`);

export const approveTimesheet = (id, managerId) =>
    api.post(`/timesheets/${id}/approve?manager_id=${managerId}`);

export const rejectTimesheet = (
    id,
    managerId,
    data
) =>
    api.post(
        `/timesheets/${id}/reject?manager_id=${managerId}`,
        data
    );

export const getPendingTimesheets = () =>
    api.get("/timesheets/status/pending");

export const getApprovedTimesheets = () =>
    api.get("/timesheets/status/approved");

export const getRejectedTimesheets = () =>
    api.get("/timesheets/status/rejected");

export const getEmployeeTimesheets = (employeeId) =>
    api.get(`/timesheets/employee/${employeeId}`);

export const getProjectTimesheets = (projectId) =>
    api.get(`/timesheets/project/${projectId}`);

// ======================================================
// Dashboard APIs
// ======================================================

export const getCeoDashboard = () =>
    api.get("/dashboard/ceo");

export const getManagerDashboard = () =>
    api.get("/dashboard/manager");

export const getEmployeeDashboard = (employeeId) =>
    api.get(`/dashboard/employee/${employeeId}`);

// ======================================================
// Report APIs
// ======================================================

export const getBillableReport = () =>
    api.get("/reports/billable");

export const getNonBillableReport = () =>
    api.get("/reports/non-billable");

export const getProjectProgressReport = () =>
    api.get("/reports/project-progress");

export const getResourceAllocationReport = () =>
    api.get("/reports/resource-allocation");

export const getTimesheetComplianceReport = () =>
    api.get("/reports/timesheet-compliance");

// ======================================================
// Axios Interceptor
// ======================================================

api.interceptors.request.use(
    (config) => {

        const token =
            localStorage.getItem("access_token");

        if (token) {
            config.headers.Authorization =
                `Bearer ${token}`;
        }

        return config;
    },
    (error) => Promise.reject(error)
);

export default api;