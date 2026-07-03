"""
===========================================================
BrainInsight AI
Preprocessing Utility
-----------------------------------------------------------
This module contains reusable image preprocessing functions
used throughout the backend.

Pipeline:
1. Read Image
2. Resize
3. Convert to Grayscale
4. Histogram Equalization
5. Gaussian Blur
6. Otsu Thresholding
7. Morphological Opening
8. Morphological Closing
===========================================================
"""

import cv2
import numpy as np
from pathlib import Path

# ==========================================================
# Configuration
# ==========================================================

IMAGE_SIZE = (256, 256)

# ==========================================================
# Read Image
# ==========================================================

def load_image(image_path: str) -> np.ndarray:
    """
    Loads an image from disk.

    Parameters
    ----------
    image_path : str

    Returns
    -------
    numpy.ndarray
    """

    image = cv2.imread(str(image_path))

    if image is None:
        raise FileNotFoundError(
            f"Unable to load image: {image_path}"
        )

    return image


# ==========================================================
# Resize Image
# ==========================================================

def resize_image(
    image: np.ndarray,
    size: tuple = IMAGE_SIZE
) -> np.ndarray:
    """
    Resize image.
    """

    return cv2.resize(image, size)


# ==========================================================
# Convert to Grayscale
# ==========================================================

def to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert BGR image to grayscale.
    """

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# ==========================================================
# Histogram Equalization
# ==========================================================

def histogram_equalization(
    gray_image: np.ndarray
) -> np.ndarray:
    """
    Improve image contrast.
    """

    return cv2.equalizeHist(gray_image)


# ==========================================================
# Gaussian Blur
# ==========================================================

def gaussian_blur(
    image: np.ndarray,
    kernel_size=(5, 5)
) -> np.ndarray:
    """
    Remove image noise.
    """

    return cv2.GaussianBlur(
        image,
        kernel_size,
        0
    )


# ==========================================================
# Otsu Thresholding
# ==========================================================

def otsu_threshold(
    image: np.ndarray
) -> np.ndarray:
    """
    Perform Otsu thresholding.
    """

    _, threshold = cv2.threshold(
        image,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return threshold


# ==========================================================
# Morphological Opening
# ==========================================================

def morphological_opening(
    image: np.ndarray,
    kernel_size=(3, 3)
) -> np.ndarray:
    """
    Remove small white noise.
    """

    kernel = np.ones(kernel_size, np.uint8)

    return cv2.morphologyEx(
        image,
        cv2.MORPH_OPEN,
        kernel
    )


# ==========================================================
# Morphological Closing
# ==========================================================

def morphological_closing(
    image: np.ndarray,
    kernel_size=(3, 3)
) -> np.ndarray:
    """
    Fill small holes.
    """

    kernel = np.ones(kernel_size, np.uint8)

    return cv2.morphologyEx(
        image,
        cv2.MORPH_CLOSE,
        kernel
    )


# ==========================================================
# Complete Preprocessing Pipeline
# ==========================================================

def preprocess_image(image_path: str) -> np.ndarray:
    """
    Complete preprocessing pipeline.

    Parameters
    ----------
    image_path : str

    Returns
    -------
    numpy.ndarray
        Final processed image.
    """

    image = load_image(image_path)

    image = resize_image(image)

    gray = to_grayscale(image)

    equalized = histogram_equalization(gray)

    blurred = gaussian_blur(equalized)

    threshold = otsu_threshold(blurred)

    opened = morphological_opening(threshold)

    processed = morphological_closing(opened)

    return processed


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    IMAGE = "../dataset/Testing/glioma/Te-gl_1.jpg"

    try:

        output = preprocess_image(IMAGE)

        print("Preprocessing Successful")
        print("Output Shape:", output.shape)

    except Exception as error:

        print(error)