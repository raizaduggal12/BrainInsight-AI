"""
===========================================================
BrainInsight AI
Main Flask Application
-----------------------------------------------------------
Entry point of the Flask backend.

Author : Raiza Duggal
===========================================================
"""

from flask import Flask, jsonify
from flask_cors import CORS

from config import (
    SECRET_KEY,
    MAX_CONTENT_LENGTH
)

from database.db import initialize_database

from routes.upload import upload_bp
from routes.predict import predict_bp
from routes.history import history_bp
from routes.report import report_bp


# ==========================================================
# Create Flask App
# ==========================================================

def create_app():
    """
    Creates and configures the Flask application.
    """

    app = Flask(__name__)

    # ------------------------------------------
    # Configuration
    # ------------------------------------------

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

    # Enable CORS for React frontend
    CORS(app)

    # ------------------------------------------
    # Initialize Database
    # ------------------------------------------

    initialize_database()

    # ------------------------------------------
    # Register Blueprints
    # ------------------------------------------

    app.register_blueprint(upload_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(report_bp)

    # ------------------------------------------
    # Home Route
    # ------------------------------------------

    @app.route("/", methods=["GET"])
    def home():

        return jsonify({

            "project": "BrainInsight AI",

            "version": "1.0",

            "status": "Running",

            "message": "BrainInsight AI Backend is running successfully."

        })

    # ------------------------------------------
    # Health Check
    # ------------------------------------------

    @app.route("/health", methods=["GET"])
    def health():

        return jsonify({

            "status": "Healthy"

        })

    return app


# ==========================================================
# Run Application
# ==========================================================

app = create_app()

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )