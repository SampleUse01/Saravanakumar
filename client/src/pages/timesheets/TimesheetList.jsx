import { useEffect, useState } from "react";
import { getTimesheets } from "../../api/apis";

export default function TimesheetList() {

  const [items, setItems] =
    useState([]);

  useEffect(() => {
    load();
  }, []);

  const load = async () => {

    const response =
      await getTimesheets();

    setItems(response.data);
  };

  return (
    <div style={{ padding: 24 }}>

      <h2>Timesheets</h2>

      <table style={{ width: "100%" }}>
        <thead>
          <tr>
            <th>Date</th>
            <th>Hours</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>

          {items.map(item => (

            <tr key={item.id}>
              <td>{item.work_date}</td>
              <td>{item.total_hours}</td>
              <td>{item.timesheet_status}</td>
            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}