"""
===========================================================
BrainInsight AI
Report Route
===========================================================
"""

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import send_file

from utils.report_generator import generate_pdf_report

report_bp = Blueprint("report", __name__)


@report_bp.route("/report", methods=["POST"])
def report():

    try:

        data = request.get_json()

        if data is None:

            return jsonify({

                "status": "error",

                "message": "JSON data not received."

            }), 400

        patient_id = data.get("patient_id", "")

        prediction = data.get("prediction", {})

        segmentation = data.get("segmentation", {})

        severity = data.get("severity", {})

        pdf_path = generate_pdf_report(

            patient_id=patient_id,

            prediction_result=prediction,

            segmentation_result=segmentation,

            severity_result=severity

        )

        return send_file(

            pdf_path,

            as_attachment=True,

            download_name=f"{patient_id}_BrainInsight_Report.pdf",

            mimetype="application/pdf"

        )

    except Exception as error:

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500