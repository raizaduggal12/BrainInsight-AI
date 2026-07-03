"""
===========================================================
BrainInsight AI
Severity Analysis Utility
-----------------------------------------------------------
Calculates a weighted severity score based on tumor
measurements extracted during segmentation.

NOTE:
This severity score is intended for educational and
research purposes only and is NOT a medical diagnosis.
===========================================================
"""

from utils.segmentation import segment_tumor


# ==========================================================
# Normalize Function
# ==========================================================

def normalize(value, max_value):
    """
    Normalize a value between 0 and 1.
    """

    value = max(0, min(value, max_value))
    return value / max_value


# ==========================================================
# Calculate Severity
# ==========================================================

def calculate_severity(measurements):
    """
    Calculate weighted severity score.

    Parameters
    ----------
    measurements : dict

    Returns
    -------
    dict
    """

    area = normalize(
        measurements["tumor_percentage"],
        100
    )

    texture = normalize(
        measurements["texture"],
        100
    )

    circularity = 1 - normalize(
        measurements["circularity"],
        1
    )

    brightness = normalize(
        measurements["brightness"],
        255
    )

    edge = normalize(
        measurements["edge_irregularity"],
        10
    )

    severity_score = (

        0.35 * area +

        0.20 * texture +

        0.15 * circularity +

        0.15 * brightness +

        0.15 * edge

    ) * 100

    severity_score = round(severity_score, 2)

    if severity_score < 35:

        risk = "Low Risk"

    elif severity_score < 70:

        risk = "Medium Risk"

    else:

        risk = "High Risk"

    return {

        "severity_score": severity_score,

        "risk_level": risk,

        "disclaimer":
        (
            "This severity score is intended "
            "for educational and research "
            "purposes only and should not "
            "be considered a medical diagnosis."
        )

    }


# ==========================================================
# Complete Pipeline
# ==========================================================

def analyze_severity(image_path):
    """
    Performs segmentation and severity analysis.
    """

    segmentation_result = segment_tumor(image_path)

    if segmentation_result["measurements"] is None:

        return {

            "error":
            "No tumor region detected."

        }

    severity = calculate_severity(

        segmentation_result["measurements"]

    )

    return {

        "measurements":
        segmentation_result["measurements"],

        "severity":
        severity

    }


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    IMAGE = "../dataset/Testing/glioma/Te-gl_1.jpg"

    result = analyze_severity(IMAGE)

    print("=" * 60)

    if "error" in result:

        print(result["error"])

    else:

        print("Severity Analysis Successful\n")

        print("Measurements")

        for key, value in result["measurements"].items():

            print(f"{key:<20}: {value}")

        print()

        print("Severity Score :",
              result["severity"]["severity_score"])

        print("Risk Level     :",
              result["severity"]["risk_level"])

    print("=" * 60)