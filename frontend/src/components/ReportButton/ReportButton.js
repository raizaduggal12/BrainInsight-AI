import "./ReportButton.css";
import { generateReport } from "../../services/api";

function ReportButton({ result }) {

    const handleDownload = async () => {

        try {

            const response = await generateReport({

                patient_id: result.patient_id,

                prediction: result.prediction,

                segmentation: result.segmentation,

                severity: result.severity

            });

            const url = window.URL.createObjectURL(
                new Blob([response.data])
            );

            const link = document.createElement("a");

            link.href = url;

            link.download =
                `${result.patient_id}_BrainInsight_Report.pdf`;

            document.body.appendChild(link);

            link.click();

            document.body.removeChild(link);

            window.URL.revokeObjectURL(url);

        }

        catch (error) {

            console.error(error);

            alert("Failed to download report.");

        }

    };

    return (

        <button
            className="report-btn"
            onClick={handleDownload}
        >
            Download Report
        </button>

    );

}

export default ReportButton;