import { useState, useContext, useEffect } from "react";
import { userContext } from "../App";
import { api} from "../utilities";
import { useNavigate } from "react-router-dom";

export const Register = () => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [estimatedYearIncome, setEstimatedYearIncome] = useState("");
  const [filingStatus, setFilingStatus] = useState("");

  const { setUser } = useContext(userContext);
  const navigate = useNavigate()
  

  useEffect(() => {
    console.log("username:  ", userName);
    console.log("password:  ", password);
    console.log("name:  ", name);
    console.log("estimatedYearIncome:  ", estimatedYearIncome);
    console.log("filingStatus: ", filingStatus);

  }, [userName, password, name, estimatedYearIncome, filingStatus]);

  const signUp = async (e) => {
    e.preventDefault();
    // "http://127.0.0.1:8000/"
    let response = await api.post("users/register/", {
      email: userName,
      password: password,
      name: name,
      estimated_year_income: estimatedYearIncome,
      filling_status: filingStatus,

    });
    console.log(response)
    // expected response
    // {"user": {"email": user.email}, "token": token.key}, status=HTTP_201_CREATED
    let user = response.data.user;
    let token = response.data.token;
    setUser(user);
    localStorage.setItem("token", token);
    navigate("homepage/");
  };

  return (
    <form onSubmit={(e) => signUp(e)}>
      <h5>Sign Up</h5>
      <input
        type="email"
        value={userName}
        onChange={(e) => setUserName(e.target.value)}
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <input 
        type="text" 
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      
      <input 
        type="number" 
        value={estimatedYearIncome}
        onChange={(e) => setEstimatedYearIncome(e.target.value)}
      />
      <select
        value={filingStatus}
        onChange={(e) => setFilingStatus(e.target.value)}
      >
        <option value="single">Single</option>
        <option value="married">Married</option>
        <option value="headOfHousehold">Head of Household</option>
      </select>
      <input type="submit" />
    </form>
  );
};
