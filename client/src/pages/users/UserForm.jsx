import {
  useEffect,
  useState
} from "react";

import {
  createUser,
  getRoles
} from "../../api/apis";

export default function UserForm() {

  const [roles,
    setRoles] =
    useState([]);

  const [form,
    setForm] =
    useState({
      employee_code: "",
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      role_id: ""
    });

  useEffect(() => {

    loadRoles();

  }, []);

  const loadRoles =
    async () => {

      const response =
        await getRoles();

      setRoles(
        response.data.data
      );

    };

  const saveUser =
    async () => {

      await createUser(form);

      alert(
        "User Created Successfully"
      );

    };

  return (
    <div>

      <h2>
        Create User
      </h2>

      <input
        placeholder="Employee Code"
        onChange={(e) =>
          setForm({
            ...form,
            employee_code:
              e.target.value
          })
        }
      />

      <input
        placeholder="First Name"
        onChange={(e) =>
          setForm({
            ...form,
            first_name:
              e.target.value
          })
        }
      />

      <input
        placeholder="Last Name"
        onChange={(e) =>
          setForm({
            ...form,
            last_name:
              e.target.value
          })
        }
      />

      <input
        placeholder="Email"
        onChange={(e) =>
          setForm({
            ...form,
            email:
              e.target.value
          })
        }
      />

      <input
        placeholder="Password"
        type="password"
        onChange={(e) =>
          setForm({
            ...form,
            password:
              e.target.value
          })
        }
      />

      <select
        onChange={(e) =>
          setForm({
            ...form,
            role_id:
              e.target.value
          })
        }
      >

        <option value="">
          Select Role
        </option>

        {roles.map((role) => (

          <option
            key={role.id}
            value={role.id}
          >
            {role.role_name}
          </option>

        ))}

      </select>

      <button
        onClick={saveUser}
      >
        Save User
      </button>

    </div>
  );
}