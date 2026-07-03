"""
===========================================================
BrainInsight AI
Prediction Utility
-----------------------------------------------------------
This module loads the trained machine learning model and
predicts the tumor class from a Brain MRI image.
===========================================================
"""

from pathlib import Path
import joblib
import numpy as np

from utils.feature_extraction import extract_features

# ==========================================================
# Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = PROJECT_ROOT / "saved_models"

MODEL_PATH = MODEL_DIR / "random_forest.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"
ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"

# ==========================================================
# Load Files Once
# ==========================================================

model = joblib.load(MODEL_PATH)

scaler = joblib.load(SCALER_PATH)

encoder = joblib.load(ENCODER_PATH)


# ==========================================================
# Prediction Function
# ==========================================================

def predict_image(image_path: str):
    """
    Predict tumor class.

    Parameters
    ----------
    image_path : str

    Returns
    -------
    dict
    """

    try:

        features = extract_features(image_path)

        features = scaler.transform([features])

        prediction = model.predict(features)[0]

        probabilities = model.predict_proba(features)[0]

        confidence = float(np.max(probabilities) * 100)

        label = encoder.inverse_transform([prediction])[0]

        return {

            "prediction": label,

            "confidence": round(confidence, 2),

            "probabilities": {

                class_name: round(float(prob) * 100, 2)

                for class_name, prob in zip(
                    encoder.classes_,
                    probabilities
                )
            }

        }

    except Exception as error:

        return {

            "error": str(error)

        }


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    IMAGE = "../dataset/Testing/glioma/Te-gl_1.jpg"

    result = predict_image(IMAGE)

    print("=" * 50)

    print(result)

    print("=" * 50)