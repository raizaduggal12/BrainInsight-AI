import React from "react";
import "./Workflow.css";

import { FaUpload, FaSlidersH, FaBrain, FaFileMedical } from "react-icons/fa";

function Workflow() {
  return (
    <div className="workflow-container">
      <h2 className="workflow-title"> <span style={{color: "#2E8BFF"}}> - - </span>How It Works <span style={{color: "#2E8BFF"}}>- -</span> </h2>

        <div className="workflow">
            <div className="step">
            <div className="circle blue">
                <FaUpload />
            </div>

            <h4>Upload MRI</h4>

            <p>Upload your brain MRI scan</p>
            </div>

            <div className="line"></div>

            <div className="step">
            <div className="circle cyan">
                <FaSlidersH />
            </div>

            <h4>Preprocessing</h4>

            <p>Image is enhanced and processed</p>
            </div>

            <div className="line"></div>

            <div className="step">
            <div className="circle purple">
                <FaBrain />
            </div>

            <h4>AI Analysis</h4>

            <p>Our AI analyzes the MRI image</p>
            </div>

            <div className="line"></div>

            <div className="step">
            <div className="circle green">
                <FaFileMedical />
            </div>

            <h4>Prediction</h4>

            <p>Get instant diagnosis report</p>
            </div>
        </div>
    </div>
  );
}

export default Workflow;
