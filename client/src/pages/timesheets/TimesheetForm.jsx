import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { createTimesheet } from "../../api/apis";



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




export default function TimesheetForm() {

  const navigate = useNavigate();

  const [form, setForm] = useState({
    employee_id: "",
    project_id: "",
    task_id: "",
    activity_type_id: "",
    total_hours: 0,
    remarks: ""
  });

  const saveTimesheet = async () => {

    await createTimesheet(form);

    navigate("/timesheets");
  };

  return (
    <div style={{ padding: 24 }}>

      <h2>Create Timesheet</h2>

      <div style={container}>

        <input
          style={input}
          placeholder="Employee Id"
          onChange={(e) =>
            setForm({
              ...form,
              employee_id: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Project Id"
          onChange={(e) =>
            setForm({
              ...form,
              project_id: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Task Id"
          onChange={(e) =>
            setForm({
              ...form,
              task_id: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Hours"
          type="number"
          onChange={(e) =>
            setForm({
              ...form,
              total_hours: e.target.value
            })
          }
        />

        <textarea
          style={input}
          placeholder="Remarks"
          onChange={(e) =>
            setForm({
              ...form,
              remarks: e.target.value
            })
          }
        />

        <button
          style={button}
          onClick={saveTimesheet}
        >
          Save Timesheet
        </button>

      </div>

    </div>
  );
}