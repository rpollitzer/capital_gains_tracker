import { useContext } from "react";
import { userContext } from "../App";
import  UserInfoBar from "../components/userbar";

export const HomePage = () => {
    const { user } = useContext(userContext);

    const userData = {
        name: "John Doe",
        contributedCapital: 5000,
        losses: 1000,
        longTermGains: 3000,
        shortTermGains: 1500,
        };
    
        return (
        <div>
            <UserInfoBar
                userName={name}
                contributedCapital={userData.contributedCapital}
                losses={userData.losses}
                longTermGains={userData.longTermGains}
                shortTermGains={userData.shortTermGains}
            />
            <h1>Welcome {user ? user.name : "Guest"}</h1>
        </div>
        );
    };