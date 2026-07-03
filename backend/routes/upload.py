"""
===========================================================
BrainInsight AI
Upload Route
-----------------------------------------------------------
Handles MRI image uploads.

Endpoint:
POST /upload
===========================================================
"""

from pathlib import Path
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

# ==========================================================
# Blueprint
# ==========================================================

upload_bp = Blueprint("upload", __name__)

# ==========================================================
# Upload Folder
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

UPLOAD_FOLDER = PROJECT_ROOT / "uploads"

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Allowed Extensions
# ==========================================================

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg"
}


# ==========================================================
# Check File Extension
# ==========================================================

def allowed_file(filename):
    """
    Check whether uploaded file is allowed.
    """

    return (

        "." in filename

        and

        filename.rsplit(".", 1)[1].lower()

        in ALLOWED_EXTENSIONS

    )


# ==========================================================
# Upload API
# ==========================================================

@upload_bp.route("/upload", methods=["POST"])
def upload_image():
    """
    Upload MRI Image.
    """

    try:

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

                "message": "Only PNG, JPG and JPEG files are allowed."

            }), 400

        filename = secure_filename(file.filename)

        filepath = UPLOAD_FOLDER / filename

        file.save(filepath)

        return jsonify({

            "status": "success",

            "message": "Image uploaded successfully.",

            "filename": filename,

            "filepath": str(filepath)

        }), 200

    except Exception as error:

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500