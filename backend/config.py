"""
===========================================================
BrainInsight AI
Configuration File
-----------------------------------------------------------
This module stores all configuration settings used
throughout the backend.

Author : Raiza Duggal
===========================================================
"""

from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

# backend/
BASE_DIR = Path(__file__).resolve().parent

# BrainInsight-AI/
PROJECT_ROOT = BASE_DIR.parent

# ==========================================================
# Dataset Paths
# ==========================================================

DATASET_DIR = PROJECT_ROOT / "dataset"

TRAIN_DIR = DATASET_DIR / "Training"

TEST_DIR = DATASET_DIR / "Testing"

PREPROCESSED_DIR = PROJECT_ROOT / "Preprocessed"

# ==========================================================
# Saved Models
# ==========================================================

MODEL_DIR = PROJECT_ROOT / "saved_models"

RANDOM_FOREST_MODEL = MODEL_DIR / "random_forest.pkl"

DECISION_TREE_MODEL = MODEL_DIR / "decision_tree.pkl"

KNN_MODEL = MODEL_DIR / "knn.pkl"

XGBOOST_MODEL = MODEL_DIR / "xgboost.pkl"

SCALER_PATH = MODEL_DIR / "scaler.pkl"

LABEL_ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"

# ==========================================================
# Output Directories
# ==========================================================

OUTPUT_DIR = PROJECT_ROOT / "outputs"

REPORT_DIR = OUTPUT_DIR / "reports"

SHAP_DIR = OUTPUT_DIR / "shap"

LIME_DIR = OUTPUT_DIR / "lime"

SEGMENTATION_DIR = OUTPUT_DIR / "segmented_images"

FEATURE_IMPORTANCE_DIR = OUTPUT_DIR / "feature_importance"

GRAPH_DIR = OUTPUT_DIR / "graphs"

# ==========================================================
# Backend Directories
# ==========================================================

UPLOAD_FOLDER = BASE_DIR / "uploads"

STATIC_FOLDER = BASE_DIR / "static"

DATABASE_PATH = BASE_DIR / "database" / "database.db"

# ==========================================================
# Flask Configuration
# ==========================================================

SECRET_KEY = "braininsight_ai_secret_key"

MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg"
}

# ==========================================================
# Image Configuration
# ==========================================================

IMAGE_SIZE = (256, 256)

# ==========================================================
# Create Required Directories
# ==========================================================

directories = [

    REPORT_DIR,

    SHAP_DIR,

    LIME_DIR,

    SEGMENTATION_DIR,

    FEATURE_IMPORTANCE_DIR,

    GRAPH_DIR,

    UPLOAD_FOLDER,

    STATIC_FOLDER,

    PREPROCESSED_DIR

]

for directory in directories:

    directory.mkdir(

        parents=True,

        exist_ok=True

    )

# ==========================================================
# Helper Function
# ==========================================================

def is_allowed_file(filename):
    """
    Check whether uploaded file extension is allowed.
    """

    return (

        "." in filename

        and

        filename.rsplit(".", 1)[1].lower()

        in ALLOWED_EXTENSIONS

    )

# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)

    print("BrainInsight AI Configuration")

    print("=" * 60)

    print("Project Root      :", PROJECT_ROOT)

    print("Dataset           :", DATASET_DIR)

    print("Saved Models      :", MODEL_DIR)

    print("Uploads           :", UPLOAD_FOLDER)

    print("Database          :", DATABASE_PATH)

    print("Reports           :", REPORT_DIR)

    print("SHAP              :", SHAP_DIR)

    print("LIME              :", LIME_DIR)

    print("=" * 60)