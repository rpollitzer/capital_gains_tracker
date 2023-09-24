import { useEffect, useState } from "react";
import "./App.css";
import { Link, Outlet } from "react-router-dom";
import { createContext } from "react";
import { api } from "./utilities";
import { useNavigate } from "react-router-dom";

export const userContext = createContext();

function App() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    console.log(user);
  }, [user]);

  const whoAmI = async () => {
    let token = localStorage.getItem("token");
    if (token) {
      api.defaults.headers.common["Authorization"] = `Token ${token}`;
      try{
        let response = await api.post("users/info/");
        setUser(response.data);
        navigate("homepage");
      }
      catch{
        setUser(null);
        // delete api.headers.common["Authorization"];
        navigate("login");

      }
    }
  };

  useEffect(() => {
    whoAmI();
  }, []);

  return (
    <div id="app">
      <header>
        <nav>
          <button>
            <Link to="/home">Home</Link>
          </button>
          <button onClick={() => setUser(null)}>Log out</button>
          <button>
            <Link to="/RegisterPage">Register</Link>
          </button>
          <button>
            <Link to="/login">Log In</Link>
          </button>
        </nav>
      </header>
      <userContext.Provider value={{ user, setUser }}>
        <Outlet />
      </userContext.Provider>
    </div>
  );
}

export default App;
