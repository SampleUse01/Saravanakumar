import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { createTask } from "../../api/apis";


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


export default function TaskForm() {

  const navigate = useNavigate();

  const [form, setForm] = useState({
    task_name: "",
    project_id: "",
    description: "",
    priority: "MEDIUM",
    planned_hours: 0,
    status: "OPEN"
  });

  const saveTask = async () => {

    await createTask(form);

    navigate("/tasks");
  };

  return (
    <div style={{ padding: 24 }}>

      <h2>Create Task</h2>

      <div style={container}>

        <input
          style={input}
          placeholder="Task Name"
          onChange={(e) =>
            setForm({
              ...form,
              task_name: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Project ID"
          onChange={(e) =>
            setForm({
              ...form,
              project_id: e.target.value
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

        <select
          style={input}
          onChange={(e) =>
            setForm({
              ...form,
              priority: e.target.value
            })
          }
        >
          <option>LOW</option>
          <option>MEDIUM</option>
          <option>HIGH</option>
          <option>CRITICAL</option>
        </select>

        <button
          style={button}
          onClick={saveTask}
        >
          Save Task
        </button>

      </div>

    </div>
  );
}