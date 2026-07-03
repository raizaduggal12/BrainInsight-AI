/*
=========================================================
BrainInsight AI
Upload Form Component
=========================================================
*/

import React, { useState } from "react";
import "./UploadForm.css";

import { predictImage } from "../../services/api";

import Loader from "../Loader/Loader";
import PredictionCard from "../PredictionCard/PredictionCard";
import ReportButton from "../ReportButton/ReportButton";

function UploadForm() {

    // ===========================================
    // States
    // ===========================================

    const [patientId, setPatientId] = useState("");

    const [image, setImage] = useState(null);

    const [preview, setPreview] = useState(null);

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState(null);

    const [error, setError] = useState("");

    // ===========================================
    // Select Image
    // ===========================================

    const handleImageChange = (event) => {

        const file = event.target.files[0];

        if (!file) return;

        setImage(file);

        setPreview(URL.createObjectURL(file));

        // Clear previous prediction
        setResult(null);

        setError("");

    };

    // ===========================================
    // Submit
    // ===========================================

    const handleSubmit = async (event) => {

        event.preventDefault();

        if (!patientId.trim()) {

            alert("Enter Patient ID");

            return;

        }

        if (!image) {

            alert("Select an MRI Image");

            return;

        }

        try {

            setLoading(true);

            setError("");

            setResult(null);

            const formData = new FormData();

            formData.append("patient_id", patientId);

            formData.append("image", image);

            const response = await predictImage(formData);

            setResult(response.data);

        }

        catch (err) {

            console.error(err);

            setError("Prediction Failed.");

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <form 
            className="upload-form"
            onSubmit={handleSubmit}
            
        >

            <label>Patient ID</label>

            <input
                type="text"
                placeholder="Enter Patient ID"
                value={patientId}
                onChange={(e) => setPatientId(e.target.value)}
            />

            <label>Upload MRI Image</label>

            <input
                type="file"
                accept=".png,.jpg,.jpeg"
                onChange={handleImageChange}
            />

            {preview && (

                <img
                    src={preview}
                    alt="MRI Preview"
                    className="preview-image"
                />

            )}

            {loading ? (

                <Loader />

            ) : (

                <button
                    type="submit"
                    disabled={!image}
                    className="predict-btn"
                >
                    Predict
                </button>

            )}

            {error && (

                <p
                    style={{
                        color: "red",
                        marginTop: "10px"
                    }}
                >
                    {error}
                </p>

            )}

            {result && (

                <>

                    <PredictionCard
                        result={result}
                    />

                    <ReportButton
                        result={result}
                    />

                </>

            )}

        </form>

    );

}

export default UploadForm;