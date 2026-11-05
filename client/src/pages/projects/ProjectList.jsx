import { useEffect, useState } from "react";

import {
  getProjects
} from "../../api/apis";

export default function ProjectList() {

  const [projects, setProjects] =
    useState([]);

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = async () => {

    const response =
      await getProjects();

    setProjects(
      response.data.data
    );
  };

  return (
    <div style={{ padding: 24 }}>

      <h2>Projects</h2>

      <table style={{ width: "100%" }}>

        <thead>
          <tr>
            <th>Code</th>
            <th>Name</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>

          {projects.map(project => (

            <tr key={project.id}>
              <td>{project.project_code}</td>
              <td>{project.project_name}</td>
              <td>{project.status}</td>
            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}