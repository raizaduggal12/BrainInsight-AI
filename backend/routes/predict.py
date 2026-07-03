"""
===========================================================
BrainInsight AI
Prediction Route
-----------------------------------------------------------
Endpoint:
POST /predict

Performs:
1. Upload Image
2. Prediction
3. Segmentation
4. Severity Analysis
5. SHAP
6. LIME
7. Save Prediction History
===========================================================
"""

from pathlib import Path

from flask import Blueprint
from flask import jsonify
from flask import request

from werkzeug.utils import secure_filename

from utils.prediction import predict_image
from utils.segmentation import segment_tumor
from utils.severity import analyze_severity
from utils.shap_utils import generate_shap
from utils.lime_utils import generate_lime

from database.db import insert_prediction


# ==========================================================
# Blueprint
# ==========================================================

predict_bp = Blueprint("predict", __name__)


# ==========================================================
# Upload Folder
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

UPLOAD_FOLDER = PROJECT_ROOT / "uploads"

UPLOAD_FOLDER.mkdir(exist_ok=True)


# ==========================================================
# Allowed Extensions
# ==========================================================

ALLOWED_EXTENSIONS = {

    "png",

    "jpg",

    "jpeg"

}


# ==========================================================
# Helper
# ==========================================================

def allowed_file(filename):

    return (

        "." in filename

        and

        filename.rsplit(".", 1)[1].lower()

        in ALLOWED_EXTENSIONS

    )


# ==========================================================
# Prediction API
# ==========================================================

@predict_bp.route("/predict", methods=["POST"])

def predict():

    try:

        # --------------------------------------------------

        if "image" not in request.files:

            return jsonify({

                "status": "error",

                "message": "No image uploaded."

            }), 400

        file = request.files["image"]

        if file.filename == "":

            return jsonify({

                "status": "error",

                "message": "No file selected."

            }), 400

        if not allowed_file(file.filename):

            return jsonify({

                "status": "error",

                "message":
                "Only PNG/JPG/JPEG supported."

            }), 400

        # --------------------------------------------------

        filename = secure_filename(file.filename)

        image_path = UPLOAD_FOLDER / filename

        file.save(image_path)

        # --------------------------------------------------
        # ML Prediction
        # --------------------------------------------------

        prediction_result = predict_image(

            str(image_path)

        )

        # --------------------------------------------------

        segmentation_result = segment_tumor(

            str(image_path)

        )

        # --------------------------------------------------

        severity_result = analyze_severity(

            str(image_path)

        )

        # --------------------------------------------------

        shap_result = generate_shap(

            str(image_path)

        )

        # --------------------------------------------------

        lime_result = generate_lime(

            str(image_path)

        )

        # --------------------------------------------------
        # Save History
        # --------------------------------------------------

        patient_id = request.form.get(

            "patient_id",

            "UNKNOWN"

        )

        insert_prediction(

            patient_id,

            prediction_result["prediction"],

            prediction_result["confidence"],

            severity_result["severity"]["risk_level"]

        )

        # --------------------------------------------------

        print(type(prediction_result))
        print(type(segmentation_result))
        print(type(severity_result))
        print(type(shap_result))
        print(type(lime_result))

        return jsonify({

            "status": "success",

            "patient_id": patient_id,

            "prediction": prediction_result,

            "segmentation": segmentation_result,

            "severity": severity_result,

            "shap": shap_result,

            "lime": lime_result

        })

    except Exception as error:

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500