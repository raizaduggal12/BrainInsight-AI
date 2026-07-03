"""
===========================================================
BrainInsight AI
Segmentation Utility
-----------------------------------------------------------
Performs tumor segmentation using OpenCV.

Pipeline
--------
1. Image Preprocessing
2. Contour Detection
3. Tumor Mask Generation
4. Bounding Box Detection
5. Tumor Measurements
6. Save Segmentation Outputs

Author : Raiza Duggal
===========================================================
"""

import cv2
import numpy as np
from pathlib import Path

from utils.preprocessing import preprocess_image

# ==========================================================
# Output Directory
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = PROJECT_ROOT / "outputs" / "segmented_images"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================================
# Find Largest Contour
# ==========================================================

def get_largest_contour(binary_image):
    """
    Returns the largest contour from a binary image.
    """

    contours, _ = cv2.findContours(
        binary_image,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        return None

    return max(contours, key=cv2.contourArea)


# ==========================================================
# Tumor Measurements
# ==========================================================

def calculate_measurements(image, contour):
    """
    Calculate tumor measurements.
    """

    area = float(cv2.contourArea(contour))

    perimeter = float(cv2.arcLength(contour, True))

    circularity = (
        4 * np.pi * area
    ) / (perimeter ** 2 + 1e-6)

    brightness = float(np.mean(image))

    texture = float(np.std(image))

    edge_irregularity = float(
        perimeter / (np.sqrt(area) + 1e-6)
    )

    tumor_percentage = float(
        (area / image.size) * 100
    )

    return {

        "area": round(area, 2),

        "tumor_percentage": round(tumor_percentage, 2),

        "perimeter": round(perimeter, 2),

        "circularity": round(float(circularity), 4),

        "brightness": round(brightness, 2),

        "texture": round(texture, 2),

        "edge_irregularity": round(edge_irregularity, 4)

    }


# ==========================================================
# Segment Tumor
# ==========================================================

def segment_tumor(image_path):
    """
    Performs tumor segmentation and saves output images.
    """

    processed = preprocess_image(image_path)

    contour = get_largest_contour(processed)

    if contour is None:

        return {

            "mask_path": None,

            "segmented_image_path": None,

            "bounding_box": None,

            "measurements": None

        }

    # ------------------------------------------------------

    mask = np.zeros_like(processed)

    cv2.drawContours(
        mask,
        [contour],
        -1,
        255,
        thickness=-1
    )

    segmented = cv2.bitwise_and(
        processed,
        mask
    )

    # ------------------------------------------------------

    x, y, w, h = cv2.boundingRect(contour)

    # ------------------------------------------------------

    measurements = calculate_measurements(
        processed,
        contour
    )

    # ------------------------------------------------------
    # Save Images
    # ------------------------------------------------------

    image_name = Path(image_path).stem

    mask_path = OUTPUT_DIR / f"{image_name}_mask.png"

    segmented_path = OUTPUT_DIR / f"{image_name}_segmented.png"

    cv2.imwrite(str(mask_path), mask)

    cv2.imwrite(str(segmented_path), segmented)

    # ------------------------------------------------------

    return {

        "mask_path": str(mask_path),

        "segmented_image_path": str(segmented_path),

        "bounding_box": {

            "x": int(x),

            "y": int(y),

            "width": int(w),

            "height": int(h)

        },

        "measurements": measurements

    }


# ==========================================================
# Draw Bounding Box
# ==========================================================

def draw_bounding_box(image_path):
    """
    Draw bounding box on original MRI image.
    """

    image = cv2.imread(image_path)

    image = cv2.resize(image, (256, 256))

    result = segment_tumor(image_path)

    if result["bounding_box"] is None:

        return image

    box = result["bounding_box"]

    cv2.rectangle(

        image,

        (box["x"], box["y"]),

        (

            box["x"] + box["width"],

            box["y"] + box["height"]

        ),

        (0, 255, 0),

        2

    )

    return image


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    IMAGE = "../dataset/Testing/glioma/Te-gl_1.jpg"

    result = segment_tumor(IMAGE)

    print("=" * 60)

    print("Segmentation Successful")

    print(result)

    print("=" * 60)