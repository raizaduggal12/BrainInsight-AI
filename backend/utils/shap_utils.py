"""
===========================================================
BrainInsight AI
SHAP Utility
-----------------------------------------------------------
Generates SHAP explanations for a single MRI prediction.

Outputs:
- summary_plot.png
- bar_plot.png

Author : Raiza Duggal
===========================================================
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import shap

from utils.feature_extraction import extract_features

# ==========================================================
# Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = PROJECT_ROOT / "saved_models"

OUTPUT_DIR = PROJECT_ROOT / "outputs" / "shap"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Load Model
# ==========================================================

model = joblib.load(MODEL_DIR / "random_forest.pkl")

scaler = joblib.load(MODEL_DIR / "scaler.pkl")

# ==========================================================
# Generate SHAP
# ==========================================================

def generate_shap(image_path):
    """
    Generates SHAP explanation for one MRI image.

    Parameters
    ----------
    image_path : str

    Returns
    -------
    dict
    """

    try:

        # ------------------------------
        # Feature Extraction
        # ------------------------------

        features = extract_features(image_path)

        features = scaler.transform([features])

        # ------------------------------
        # SHAP
        # ------------------------------

        explainer = shap.TreeExplainer(model)

        shap_values = explainer.shap_values(features)

        # ------------------------------
        # Summary Plot
        # ------------------------------

        plt.figure(figsize=(8,6))

        shap.summary_plot(

            shap_values,

            features,

            show=False

        )

        summary_path = OUTPUT_DIR / "summary_plot.png"

        plt.tight_layout()

        plt.savefig(summary_path, dpi=300)

        plt.close()

        # ------------------------------
        # Bar Plot
        # ------------------------------

        plt.figure(figsize=(8,6))

        shap.summary_plot(

            shap_values,

            features,

            plot_type="bar",

            show=False

        )

        bar_path = OUTPUT_DIR / "bar_plot.png"

        plt.tight_layout()

        plt.savefig(bar_path, dpi=300)

        plt.close()

        return {

            "status": "success",

            "summary_plot": str(summary_path),

            "bar_plot": str(bar_path)

        }

    except Exception as error:

        return {

            "status": "error",

            "message": str(error)

        }


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    IMAGE = "../dataset/Testing/glioma/Te-gl_1.jpg"

    result = generate_shap(IMAGE)

    print("=" * 60)

    print(result)

    print("=" * 60)