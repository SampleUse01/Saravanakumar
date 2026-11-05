import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { createClient } from "../../api/apis";


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


export default function ClientForm() {

  const navigate = useNavigate();

  const [form, setForm] = useState({
    client_name: "",
    contact_person: "",
    email: "",
    phone: "",
    address: ""
  });

  const saveClient = async () => {

    await createClient(form);

    navigate("/clients");
  };

  return (
    <div style={{ padding: 24 }}>

      <h2>Create Client</h2>

      <div style={container}>

        <input
          style={input}
          placeholder="Client Name"
          onChange={(e) =>
            setForm({
              ...form,
              client_name: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Contact Person"
          onChange={(e) =>
            setForm({
              ...form,
              contact_person: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Email"
          onChange={(e) =>
            setForm({
              ...form,
              email: e.target.value
            })
          }
        />

        <input
          style={input}
          placeholder="Phone"
          onChange={(e) =>
            setForm({
              ...form,
              phone: e.target.value
            })
          }
        />

        <textarea
          style={input}
          placeholder="Address"
          onChange={(e) =>
            setForm({
              ...form,
              address: e.target.value
            })
          }
        />

        <button
          style={button}
          onClick={saveClient}
        >
          Save Client
        </button>

      </div>

    </div>
  );
}