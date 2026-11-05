import { useEffect, useState } from "react";

import {
  getCeoDashboard,
  getManagerDashboard,
  getEmployeeDashboard
} from "../../api/apis";

export default function Dashboard() {

  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);

  const role =
    localStorage.getItem("role");

  const employeeId =
    localStorage.getItem("employee_id");

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {

    try {

      let response;

      if (role === "SUPER_ADMIN") {

        response =
          await getCeoDashboard();

      } else if (
        role === "MANAGER"
      ) {

        response =
          await getManagerDashboard();

      } else {

        response =
          await getEmployeeDashboard(
            employeeId
          );
      }

      setData(
        response.data
      );

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }
  };

  if (loading) {

    return (
      <div
        style={{
          padding: "30px",
          fontSize: "16px"
        }}
      >
        Loading Dashboard...
      </div>
    );
  }

  return (
    <div
      style={{
        padding: "30px",
        backgroundColor: "#ffffff",
        minHeight: "100vh"
      }}
    >
      <div
        style={{
          marginBottom: "30px"
        }}
      >
        <h1
          style={{
            margin: 0,
            color: "#000",
            fontSize: "28px"
          }}
        >
          Dashboard
        </h1>

        <p
          style={{
            color: "#666",
            marginTop: "8px"
          }}
        >
          Welcome to PTMS
        </p>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit,minmax(250px,1fr))",
          gap: "20px"
        }}
      >

        {role === "SUPER_ADMIN" && (
          <>
            <DashboardCard
              title="Total Clients"
              value={
                data.total_clients || 0
              }
            />

            <DashboardCard
              title="Total Projects"
              value={
                data.total_projects || 0
              }
            />

            <DashboardCard
              title="Active Projects"
              value={
                data.active_projects || 0
              }
            />

            <DashboardCard
              title="Completed Projects"
              value={
                data.completed_projects || 0
              }
            />

            <DashboardCard
              title="Employees"
              value={
                data.total_employees || 0
              }
            />

            <DashboardCard
              title="Billable Hours"
              value={
                data.billable_hours || 0
              }
            />

            <DashboardCard
              title="Non Billable Hours"
              value={
                data.non_billable_hours || 0
              }
            />
          </>
        )}

        {role === "MANAGER" && (
          <>
            <DashboardCard
              title="Projects"
              value={
                data.allocated_projects || 0
              }
            />

            <DashboardCard
              title="Team Members"
              value={
                data.team_members || 0
              }
            />

            <DashboardCard
              title="Pending Approvals"
              value={
                data.pending_timesheets || 0
              }
            />

            <DashboardCard
              title="Delayed Tasks"
              value={
                data.delayed_tasks || 0
              }
            />

            <DashboardCard
              title="Task Completion"
              value={
                data.task_completion || 0
              }
            />
          </>
        )}

        {role === "EMPLOYEE" && (
          <>
            <DashboardCard
              title="Assigned Tasks"
              value={
                data.assigned_tasks || 0
              }
            />

            <DashboardCard
              title="Pending Tasks"
              value={
                data.pending_tasks || 0
              }
            />

            <DashboardCard
              title="Completed Tasks"
              value={
                data.completed_tasks || 0
              }
            />

            <DashboardCard
              title="Weekly Hours"
              value={
                data.weekly_hours || 0
              }
            />

            <DashboardCard
              title="Utilization %"
              value={
                data.utilization || 0
              }
            />
          </>
        )}

      </div>
    </div>
  );
}

function DashboardCard({
  title,
  value
}) {
  return (
    <div
      style={{
        border: "1px solid #e5e5e5",
        borderRadius: "10px",
        padding: "25px",
        backgroundColor: "#fff"
      }}
    >
      <p
        style={{
          margin: 0,
          color: "#666",
          fontSize: "14px"
        }}
      >
        {title}
      </p>

      <h2
        style={{
          marginTop: "15px",
          marginBottom: 0,
          color: "#000"
        }}
      >
        {value}
      </h2>
    </div>
  );
}