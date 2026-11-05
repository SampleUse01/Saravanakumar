import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getUsers,
  deleteUser
} from "../../api/apis";

export default function UserList() {

  const navigate = useNavigate();

  const [users, setUsers] = useState([]);

  useEffect(() => {
    loadUsers();
  }, []);

  const loadUsers = async () => {
    const response = await getUsers();
    setUsers(response.data.data || []);
  };

  const removeUser = async (id) => {

    if (!window.confirm("Delete User ?"))
      return;

    await deleteUser(id);

    loadUsers();
  };

  return (
    <div style={{ padding: 24 }}>

      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          marginBottom: 20
        }}
      >
        <h2>Users</h2>

        <button
          onClick={() =>
            navigate("/users/create")
          }
          style={{
            background: "#000",
            color: "#fff",
            border: "none",
            padding: "10px 16px",
            cursor: "pointer"
          }}
        >
          Add User
        </button>
      </div>

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse"
        }}
      >
        <thead>
          <tr>
            <th style={th}>Code</th>
            <th style={th}>Name</th>
            <th style={th}>Email</th>
            <th style={th}>Action</th>
          </tr>
        </thead>

        <tbody>

          {users.map(user => (

            <tr key={user.id}>

              <td style={td}>
                {user.employee_code}
              </td>

              <td style={td}>
                {user.first_name}
              </td>

              <td style={td}>
                {user.email}
              </td>

              <td style={td}>

                <button
                  onClick={() =>
                    navigate(
                      `/users/edit/${user.id}`
                    )
                  }
                >
                  Edit
                </button>

                {" "}

                <button
                  onClick={() =>
                    removeUser(user.id)
                  }
                >
                  Delete
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

const th = {
  textAlign: "left",
  borderBottom: "1px solid #ddd",
  padding: 12
};

const td = {
  padding: 12,
  borderBottom: "1px solid #eee"
};