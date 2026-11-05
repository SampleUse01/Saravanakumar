import { useEffect, useState } from "react";
import { getRoles } from "../../api/apis";

export default function RoleList() {

  const [roles, setRoles] =
    useState([]);

  useEffect(() => {
    loadRoles();
  }, []);

  const loadRoles = async () => {

    const response =
      await getRoles();

    setRoles(
      response.data.data
    );
  };

  return (
    <div style={{ padding: 24 }}>

      <h2>Roles</h2>

      {
        roles.map(role => (

          <div
            key={role.id}
            style={{
              border: "1px solid #ddd",
              padding: 12,
              marginBottom: 10
            }}
          >
            {role.role_name}
          </div>

        ))
      }

    </div>
  );
}