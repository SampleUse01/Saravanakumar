import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getClients
} from "../../api/apis";

export default function ClientList() {

  const navigate = useNavigate();

  const [clients, setClients] =
    useState([]);

  useEffect(() => {
    loadClients();
  }, []);

  const loadClients = async () => {

    const response =
      await getClients();

    setClients(
      response.data.data
    );
  };

  return (
    <div style={{ padding: 24 }}>

      <div
        style={{
          display: "flex",
          justifyContent: "space-between"
        }}
      >
        <h2>Clients</h2>

        <button
          onClick={() =>
            navigate("/clients/create")
          }
        >
          Add Client
        </button>
      </div>

      <table style={{ width: "100%" }}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Contact</th>
            <th>Email</th>
          </tr>
        </thead>

        <tbody>

          {
            clients.map(client => (

              <tr key={client.id}>

                <td>
                  {client.client_name}
                </td>

                <td>
                  {client.contact_person}
                </td>

                <td>
                  {client.email}
                </td>

              </tr>

            ))
          }

        </tbody>
      </table>

    </div>
  );
}