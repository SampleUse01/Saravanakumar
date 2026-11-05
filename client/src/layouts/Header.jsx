import {
  Link
} from "react-router-dom";

export default function Sidebar() {
  return (
    <div className="sidebar">

      <h2>PTMS</h2>

      <ul>

        <li>
          <Link to="/dashboard">
            Dashboard
          </Link>
        </li>

        <li>
          <Link to="/users">
            Users
          </Link>
        </li>

        <li>
          <Link to="/clients">
            Clients
          </Link>
        </li>

        <li>
          <Link to="/projects">
            Projects
          </Link>
        </li>

        <li>
          <Link to="/allocations">
            Allocations
          </Link>
        </li>

        <li>
          <Link to="/tasks">
            Tasks
          </Link>
        </li>

        <li>
          <Link to="/timesheets">
            Timesheets
          </Link>
        </li>

        <li>
          <Link to="/reports">
            Reports
          </Link>
        </li>

      </ul>

    </div>
  );
}