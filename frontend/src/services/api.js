import axios from "axios";

/*
=========================================
BrainInsight Backend URL
=========================================
*/

const API = axios.create({

    baseURL: "http://127.0.0.1:5000"

});

/*
=========================================
Upload & Predict
=========================================
*/

export const predictImage = (formData) =>

    API.post("/predict", formData);

/*
=========================================
Prediction History
=========================================
*/

export const getHistory = () =>

    API.get("/history");

/*
=========================================
Generate Report
=========================================
*/

export const generateReport = (data) =>

    API.post("/report", data, {

        responseType: "blob"

    });