import React from "react";

function About() {

    return (

        <div
            className="page"
            style={{
                minHeight: "85vh",
                paddingTop: "100px",fontSize:"25px",color:"white" 
            }}
        >

            <h1 style={{ fontSize: "50px", color: "white"  }}> About BrainInsight <span style={{ color: "#2E8BFF" }}>AI</span></h1>

            <p style={{color:"grey"}}>

                BrainInsight AI is a Machine Learning based web application
                that detects brain tumors from MRI images.

            </p>

            <br />

            <h2 style={{color:"green"}}>Project Features : </h2>

            <ul>

                <li>Brain MRI Image Upload</li>

                <li>Tumor Classification</li>

                <li>Tumor Segmentation</li>

                <li>Severity Analysis</li>

                <li>Prediction History</li>

                <li>PDF Report Generation</li>

                <li>Explainable AI (SHAP & LIME)</li>

            </ul>

            <br />

            <h2 style={{color:"green"}}>Technology Stack : </h2>

            <ul>

                <li>React.js</li>

                <li>Flask</li>

                <li>Python</li>

                <li>Scikit-Learn</li>

                <li>OpenCV</li>

                <li>SQLite</li>

            </ul>

        </div>

    );

}

export default About;