import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { login } from "../../api/apis";

export default function Login() {

  const navigate = useNavigate();

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const handleLogin = async () => {

    try {

      const response =
        await login({
          email,
          password
        });

      localStorage.setItem(
        "access_token",
        response.data.access_token
      );

      localStorage.setItem(
        "refresh_token",
        response.data.refresh_token
      );

      navigate("/dashboard");

    } catch {

      alert("Invalid Credentials");

    }

  };

  return (
    <div className="login-container">

      <div className="login-card">

        <h2>
          Login
        </h2>

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <button
          onClick={handleLogin}
        >
          Login
        </button>

      </div>

    </div>
  );
}
