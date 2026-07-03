"""
===========================================================
BrainInsight AI
History Route
-----------------------------------------------------------
Endpoints

GET     /history
GET     /history/<id>
DELETE  /history
===========================================================
"""

from flask import Blueprint
from flask import jsonify

from database.db import (
    get_prediction_history,
    clear_history
)

# ==========================================================
# Blueprint
# ==========================================================

history_bp = Blueprint("history", __name__)

# ==========================================================
# Get Complete History
# ==========================================================

@history_bp.route("/history", methods=["GET"])
def history():

    try:

        history = get_prediction_history()

        return jsonify({

            "status": "success",

            "total_records": len(history),

            "history": history

        }), 200

    except Exception as error:

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500


# ==========================================================
# Get Single Record
# ==========================================================

@history_bp.route("/history/<int:record_id>", methods=["GET"])
def single_history(record_id):

    try:

        history = get_prediction_history()

        record = None

        for item in history:

            if item["id"] == record_id:

                record = item

                break

        if record is None:

            return jsonify({

                "status": "error",

                "message": "Record not found."

            }), 404

        return jsonify({

            "status": "success",

            "record": record

        }), 200

    except Exception as error:

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500


# ==========================================================
# Delete Complete History
# ==========================================================

@history_bp.route("/history", methods=["DELETE"])
def delete_history():

    try:

        clear_history()

        return jsonify({

            "status": "success",

            "message": "Prediction history cleared successfully."

        }), 200

    except Exception as error:

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500