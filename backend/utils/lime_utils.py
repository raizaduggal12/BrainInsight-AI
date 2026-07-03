"""
===========================================================
BrainInsight AI
LIME Utility
-----------------------------------------------------------
Generates LIME explanations for a single MRI prediction.

Outputs:
- lime_report.html
- lime_feature_weights.png

Author : Raiza Duggal
===========================================================
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path

import joblib
import numpy as np
import matplotlib.pyplot as plt

from lime.lime_tabular import LimeTabularExplainer

from utils.feature_extraction import extract_features

# ==========================================================
# Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = PROJECT_ROOT / "saved_models"

OUTPUT_DIR = PROJECT_ROOT / "outputs" / "lime"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Load Model
# ==========================================================

model = joblib.load(MODEL_DIR / "random_forest.pkl")

scaler = joblib.load(MODEL_DIR / "scaler.pkl")

encoder = joblib.load(MODEL_DIR / "label_encoder.pkl")

X = np.load(PROJECT_ROOT / "outputs" / "X.npy")

# ==========================================================
# LIME Generator
# ==========================================================

def generate_lime(image_path):
    """
    Generates LIME explanation for one MRI image.
    """

    try:

        # ----------------------------------------

        features = extract_features(image_path)

        features = scaler.transform([features])

        # ----------------------------------------

        explainer = LimeTabularExplainer(

            training_data=X,

            feature_names=[
                f"Feature_{i}"
                for i in range(X.shape[1])
            ],

            class_names=list(
                encoder.classes_
            ),

            mode="classification"

        )

        # ----------------------------------------

        explanation = explainer.explain_instance(

            features[0],

            model.predict_proba,

            num_features=15

        )

        # ----------------------------------------

        html_path = OUTPUT_DIR / "lime_report.html"

        explanation.save_to_file(

            str(html_path)

        )

        # ----------------------------------------

        fig = explanation.as_pyplot_figure()

        plot_path = OUTPUT_DIR / "lime_feature_weights.png"

        fig.savefig(

            plot_path,

            dpi=300,

            bbox_inches="tight"

        )

        plt.close(fig)

        # ----------------------------------------

        return {

            "status": "success",

            "html_report": str(html_path),

            "feature_plot": str(plot_path)

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

    result = generate_lime(IMAGE)

    print("=" * 60)

    print(result)

    print("=" * 60)