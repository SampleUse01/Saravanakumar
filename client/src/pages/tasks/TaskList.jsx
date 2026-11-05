import { useEffect, useState } from "react";
import { getTasks } from "../../api/apis";

export default function TaskList() {

  const [tasks, setTasks] =
    useState([]);

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {

    const response =
      await getTasks();

    setTasks(
      response.data
    );
  };

  return (
    <div style={{ padding: 24 }}>

      <h2>Tasks</h2>

      <table style={{ width: "100%" }}>

        <thead>

          <tr>
            <th>Task</th>
            <th>Status</th>
            <th>Priority</th>
          </tr>

        </thead>

        <tbody>

          {tasks.map(task => (

            <tr key={task.id}>
              <td>{task.task_name}</td>
              <td>{task.status}</td>
              <td>{task.priority}</td>
            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}