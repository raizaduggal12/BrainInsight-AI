import React, { useEffect, useState } from "react";

import HistoryTable from "../components/HistoryTable/HistoryTable";

import { getHistory } from "../services/api";

function History() {

    const [history, setHistory] = useState([]);

    useEffect(() => {

        async function fetchHistory() {

            try {

                const response = await getHistory();

                setHistory(response.data.history);

            }

            catch (error) {

                console.error(error);

            }

        }

        fetchHistory();

    }, []);

    return (

        <div
            className="page"
            style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                minHeight: "85vh",
                paddingTop: "100px",
                color: "white"
            }}
        >

            <h1 style={{ fontSize: "50px", color: "white"  }}> Prediction History</h1>

            <p className="subtitle">

                View all previously predicted Brain MRI reports.

            </p>

            <HistoryTable history={history} />

        </div>

    );

}

export default History;