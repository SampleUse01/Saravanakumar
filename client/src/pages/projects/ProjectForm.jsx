import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { createProject } from "../../api/apis";


const container = {
  display: "flex",
  flexDirection: "column",
  gap: "15px",
  maxWidth: "600px",
  border: "1px solid #ddd",
  padding: "20px",
  background: "#fff"
};

const input = {
  padding: "12px",
  border: "1px solid #ddd",
  outline: "none"
};

const button = {
  background: "#000",
  color: "#fff",
  border: "none",
  padding: "12px",
  cursor: "pointer"
};


export default function ProjectForm() {

  const navigate = useNavigate();

  const [form, setForm] = useState({
    client_id: "",
    project_code: "",
    project_name: "",
    description: "",
    budget: 0,
    planned_hours: 0,
    status: "NOT_STARTED"
  });

  const saveProject = async () => {

    await createProject(form);

    navigate("/projects");
  };

  return (
    <div style={{ padding: 24 }}>

      <h2>Create Project</h2>

      <div style={container}>

        <input
          style={input}
          placeholder="Client Id"
          onChange={(e) =>
            setForm({
              ...form,
              client_id: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Project Code"
          onChange={(e) =>
            setForm({
              ...form,
              project_code: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Project Name"
          onChange={(e) =>
            setForm({
              ...form,
              project_name: e.target.value
            })
          }
        />

        <textarea
          style={input}
          placeholder="Description"
          onChange={(e) =>
            setForm({
              ...form,
              description: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Budget"
          type="number"
          onChange={(e) =>
            setForm({
              ...form,
              budget: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Planned Hours"
          type="number"
          onChange={(e) =>
            setForm({
              ...form,
              planned_hours: e.target.value
            })
          }
        />

        <button
          style={button}
          onClick={saveProject}
        >
          Save Project
        </button>

      </div>

    </div>
  );
}