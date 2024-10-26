// src/index.js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";

// Utiliser `createRoot` au lieu de `render`
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
   <React.StrictMode >
    <App/>
    </React.StrictMode>
);