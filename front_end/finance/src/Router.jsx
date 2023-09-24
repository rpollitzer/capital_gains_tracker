import { createBrowserRouter } from "react-router-dom";
import { HomePage } from "./pages/HomePage"
import { LogInPage } from "./pages/LogIn";
import { Register } from "./pages/RegisterPage";
import App from "./App";


export const router = createBrowserRouter([
    {
        path: "/",
        element: < App />,
        children: [
            {
                index: true,
                element: <Register/>,
            },
            {
                path: "login",
                element: <LogInPage/>,
            },
            {
                path: "homepage",
                element:<HomePage/>,
            },
            
        ],
    },
]);