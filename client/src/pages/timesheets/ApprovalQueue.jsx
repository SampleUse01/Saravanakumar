import { useEffect, useState } from "react";

import {
  getPendingTimesheets
} from "../../api/apis";

export default function ApprovalQueue() {

  const [items, setItems] =
    useState([]);

  useEffect(() => {
    load();
  }, []);

  const load = async () => {

    const response =
      await getPendingTimesheets();

    setItems(response.data);
  };

  return (
    <div style={{ padding: 24 }}>

      <h2>
        Pending Approvals
      </h2>

      {items.map(item => (

        <div
          key={item.id}
          style={{
            border: "1px solid #ddd",
            padding: 12,
            marginBottom: 10
          }}
        >
          {item.employee_id}
        </div>

      ))}

    </div>
  );
}