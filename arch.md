Project Timeline and Activity management system



Super Admin --> CEO --> Access to onboard an client or Project --> allocates more than one projects to the managers as percentage based like 20 - 20 - 60 

Admins --> Managers --> now he three projects which is allocated by the CEO (Super Admin) and manager allocates the task to the employees they can be one or more projects and manager have to set the timeline for the projects

User -- > Employee --> they can log the daily task using the timesheet --> with this have to keep the conditions like resource allocation -->project status and task status -->employee overutilization and underutilization


Condition to check:

1.they should able to log the activities of the employee and priority of the task , meetings 
2. should automaically calculate the efforts hours , billable and non-billable and timesheet overlap and track progress
3. should manager have an dashboard to see the relavent information and for employee and CEO
4. for login use the jwt with refresh token




SUPER ADMIN (CEO)
│
├── Clients
│
├── Projects
│
├── Resource Allocation
│
└── Portfolio Dashboard

MANAGER
│
├── Project Timeline
├── Milestones
├── Tasks
├── Team Allocation
├── Timesheet Approval
└── Team Dashboard

EMPLOYEE
│
├── Timesheet Entry
├── Daily Activities
├── Task Updates
├── Meetings
└── Self Dashboard

SYSTEM
│
├── Utilization Engine
├── Progress Engine
├── Overlap Detection
├── Notifications
└── Reporting




Recommended Build Order


Server:


Auth Module
User Module
Client Module
Project Module
Allocation Module
Task Module
Timesheet Module (Approval Workflow)
Dashboard Module
Reporting Module



Admin Login:

  "email": "admin@example.com",
  "password": "admin",



Client:

UserManagement.jsx
ClientManagement.jsx
ProjectManagement.jsx
AllocationManagement.jsx
TaskManagement.jsx
TimesheetManagement.jsx