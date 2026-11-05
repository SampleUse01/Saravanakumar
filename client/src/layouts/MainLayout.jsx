import { Outlet } from "react-router-dom";

import Sidebar from "./Sidebar";
import Header from "./Header";

export default function MainLayout() {
  return (
    <div className="layout">

      <Sidebar />

      <div className="content">

        <Header />

        <div className="page-body">
          <Outlet />
        </div>

      </div>

    </div>
  );
}