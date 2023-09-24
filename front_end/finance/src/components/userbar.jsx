import React from "react";

const UserInfoBar = ({
    userName,
    contributedCapital,
    losses,
    longTermGains,
    shortTermGains,
}) => {
    return (
    <div className="user-info-bar">
        <p>{userName}</p>
        <p>Contributed Capital: ${contributedCapital}</p>
        <p>Losses: ${losses}</p>
        <p>Long-term Gains: ${longTermGains}</p>
        <p>Short-term Gains: ${shortTermGains}</p>
    </div>
    );
};

export default UserInfoBar;
