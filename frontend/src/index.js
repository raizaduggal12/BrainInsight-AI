/*
=========================================================
BrainInsight AI
React Entry Point
---------------------------------------------------------
This is the first file executed when the React
application starts.

Responsibilities:
1. Render the App component
2. Import global styles
=========================================================
*/

import React from "react";
import "./App.css";
import ReactDOM from "react-dom/client";

import "./styles/global.css";

import App from "./App";

// =========================================================
// Create Root
// =========================================================

const root = ReactDOM.createRoot(

    document.getElementById("root")

);

// =========================================================
// Render Application
// =========================================================

root.render(

    <React.StrictMode>

        <App />

    </React.StrictMode>

);