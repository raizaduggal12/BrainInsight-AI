import React from "react";

import UploadForm from "../components/UploadForm/UploadForm";

import Workflow from "../components/Workflow/Workflow";

function Home() {

    return (

        <div
            className="page"
            style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                minHeight: "85vh",
                paddingTop: "200px"
            }}
        >

            <h1 style={{ fontSize: "50px", color: "white"  }}> BrainInsight <span style={{ color: "#2E8BFF" }}>AI</span> </h1>

            <p className="subtitle">

                Brain MRI Tumor Detection using Machine Learning

            </p>

            <UploadForm />

            <Workflow />

        </div>


    );

}

export default Home;