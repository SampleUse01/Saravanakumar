import { useEffect, useState } from "react";
import { getAllocations } from "../../api/apis";

export default function AllocationList() {

  const [allocations, setAllocations] =
    useState([]);

  useEffect(() => {
    load();
  }, []);

  const load = async () => {

    const response =
      await getAllocations();

    setAllocations(
      response.data
    );
  };

  return (
    <div style={{ padding: 24 }}>

      <h2>Allocations</h2>

      <table style={{ width: "100%" }}>
        <thead>
          <tr>
            <th>Project</th>
            <th>User</th>
            <th>Allocation %</th>
          </tr>
        </thead>

        <tbody>

          {allocations.map(item => (

            <tr key={item.id}>
              <td>{item.project_id}</td>
              <td>{item.user_id}</td>
              <td>{item.allocation_percentage}</td>
            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}