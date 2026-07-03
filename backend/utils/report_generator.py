"""
===========================================================
BrainInsight AI
Report Generator Utility
-----------------------------------------------------------
Generates a professional PDF report containing:

- Patient Information
- Prediction
- Confidence
- Tumor Measurements
- Severity Analysis
- Medical Disclaimer

===========================================================
"""

from pathlib import Path
from datetime import datetime

from reportlab.lib import styles
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


# ==========================================================
# Output Folder
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

REPORT_FOLDER = PROJECT_ROOT / "outputs" / "reports"

REPORT_FOLDER.mkdir(parents=True, exist_ok=True)


# ==========================================================
# Generate PDF Report
# ==========================================================

def generate_pdf_report(
        patient_id,
        prediction_result,
        segmentation_result,
        severity_result
):
    """
    Generates BrainInsight AI PDF Report.
    """

    pdf_name = f"{patient_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    pdf_path = REPORT_FOLDER / pdf_name

    styles = getSampleStyleSheet()

    document = SimpleDocTemplate(str(pdf_path))

    elements = []

    # ------------------------------------------------------

    elements.append(
        Paragraph(
            "BrainInsight AI Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # ------------------------------------------------------

    elements.append(
        Paragraph(
            f"<b>Patient ID:</b> {patient_id}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Date:</b> {datetime.now()}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # ------------------------------------------------------

    prediction_table = [

        ["Prediction", prediction_result["prediction"]],

        ["Confidence",
         f'{prediction_result["confidence"]:.2f}%']

    ]

    table = Table(prediction_table)

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8)

        ])

    )

    elements.append(
        Paragraph(
            "<b>Prediction Result</b>",
            styles["Heading2"]
        )
    )

    elements.append(table)

    elements.append(Spacer(1, 20))

    # ------------------------------------------------------

    elements.append(

        Paragraph(
            "<b>Tumor Measurements</b>",
            styles["Heading2"]
        )

    )

    measurement_table = []

    for key, value in segmentation_result[
        "measurements"
    ].items():

        measurement_table.append(

            [key, str(value)]

        )

    table = Table(measurement_table)

    table.setStyle(

        TableStyle([

            ("GRID", (0, 0), (-1, -1), 1, colors.grey),

            ("BACKGROUND", (0, 0), (-1, -1), colors.beige)

        ])

    )

    elements.append(table)

    elements.append(Spacer(1, 20))

    # ------------------------------------------------------

    elements.append(

        Paragraph(
            "<b>Severity Analysis</b>",
            styles["Heading2"]
        )

    )

    elements.append(

        Paragraph(

            f"Severity Score : "

            f"{severity_result['severity']['severity_score']}",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            f"Risk Level : "

            f"{severity_result['severity']['risk_level']}",

            styles["BodyText"]

        )

    )

    elements.append(Spacer(1, 20))

    # ------------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Doctor Note</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            "Please consult a qualified radiologist "

            "or neurologist for professional medical "

            "evaluation.",

            styles["BodyText"]

        )

    )

    elements.append(Spacer(1, 20))

    # ------------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Disclaimer</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            "This system is intended for educational "

            "and research purposes only and should "

            "not be considered a substitute for "

            "professional medical diagnosis.",

            styles["BodyText"]

        )

    )

    elements.append(Spacer(1, 20))

    # ------------------------------------------------------
    # SHAP Explanation
    # ------------------------------------------------------

    elements.append(

        Paragraph(

            "<b>SHAP Explanation</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            "SHAP (SHapley Additive exPlanations) was used to identify "

            "which extracted image features contributed the most towards "

            "the model's final prediction.",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            f"Predicted Tumor Type : "

            f"{prediction_result['prediction']}",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            "Higher SHAP values indicate features that positively "

            "influenced the prediction, whereas lower values indicate "

            "features with lesser contribution.",

            styles["BodyText"]

        )

    )

    elements.append(Spacer(1, 20))

    # ------------------------------------------------------
    # LIME Explanation
    # ------------------------------------------------------

    elements.append(

        Paragraph(

            "<b>LIME Explanation</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            "LIME (Local Interpretable Model-agnostic Explanations) "

            "was applied to explain this individual MRI prediction. "

            "It highlights the image regions and extracted features "

            "that most influenced the classifier's decision for this patient.",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            f"Model Prediction : "

            f"{prediction_result['prediction']}",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            "The generated explanation helps clinicians understand "

            "why the machine learning model predicted the given tumor "

            "class for this MRI image.",

            styles["BodyText"]

        )

    )

    elements.append(Spacer(1, 20))

    

    # ------------------------------------------------------

    document.build(elements)

    return str(pdf_path)


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    prediction = {

        "prediction": "Glioma",

        "confidence": 97.84

    }

    segmentation = {

        "measurements": {

            "area": 8452,

            "tumor_percentage": 18.7,

            "perimeter": 422,

            "circularity": 0.72,

            "brightness": 132,

            "texture": 41.6,

            "edge_irregularity": 4.15

        }

    }

    severity = {

        "severity": {

            "severity_score": 51.28,

            "risk_level": "Medium Risk"

        }

    }

    report = generate_pdf_report(

        patient_id="PAT001",

        prediction_result=prediction,

        segmentation_result=segmentation,

        severity_result=severity

    )

    


    print("=" * 50)

    print("PDF Generated Successfully")

    print(report)

    print("=" * 50)