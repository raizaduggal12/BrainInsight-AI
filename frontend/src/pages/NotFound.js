import React from "react";

import { Link } from "react-router-dom";

function NotFound() {

    return (

        <div className="page">

            <h1>404</h1>

            <h2>Page Not Found</h2>

            <p>

                The page you are trying to access does not exist.

            </p>

            <br />

            <Link to="/">

                Go Back Home

            </Link>

        </div>

    );

}

export default NotFound;