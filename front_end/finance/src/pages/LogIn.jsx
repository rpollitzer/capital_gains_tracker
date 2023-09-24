import { useState, useContext } from "react";
import { userContext } from "../App";
import { api } from "../utilities.jsx";
import { useNavigate } from "react-router-dom";

export const LogInPage = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const { setUser } = useContext(userContext);

    const navigate = useNavigate();
    
    function API(e){
        e.preventDefault()
        async function loginRequest(){
            try{
                console.log(email)
                console.log(password)
            const response = await api.post(`users/login/`, {
                "email": email,
                "password": password,
                });
                setUser(email)
                navigate("/homepage");
            }
            catch(err){
                console.log(err)
                console.log("Not Working")

            }
        }
        loginRequest()
    }

    return (
    <form onSubmit={(e) => API(e)}>
        <h5>Log In</h5>
        <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
        />
        <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
        />
        <input type="submit"/>

    </form>
    );
};
