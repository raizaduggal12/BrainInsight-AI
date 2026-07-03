"""
===========================================================
BrainInsight AI
Feature Extraction Utility
-----------------------------------------------------------
This module extracts handcrafted features from a
preprocessed brain MRI image.

Features:
1. HOG
2. LBP
3. GLCM
4. Hu Moments
5. Shape Features
6. Histogram Features
7. Statistical Texture Features
===========================================================
"""

import cv2
import numpy as np

from skimage.feature import (
    hog,
    local_binary_pattern,
    graycomatrix,
    graycoprops,
)

from utils.preprocessing import preprocess_image


# ==========================================================
# HOG Features
# ==========================================================

def extract_hog(image):

    return hog(
        image,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        feature_vector=True
    )


# ==========================================================
# LBP Features
# ==========================================================

def extract_lbp(image):

    lbp = local_binary_pattern(
        image,
        P=8,
        R=1,
        method="uniform"
    )

    hist, _ = np.histogram(
        lbp.ravel(),
        bins=np.arange(0, 11),
        range=(0, 10)
    )

    hist = hist.astype("float32")
    hist /= hist.sum() + 1e-6

    return hist


# ==========================================================
# GLCM Features
# ==========================================================

def extract_glcm(image):

    glcm = graycomatrix(
        image,
        distances=[1],
        angles=[0],
        symmetric=True,
        normed=True
    )

    return np.array([
        graycoprops(glcm, "contrast")[0, 0],
        graycoprops(glcm, "correlation")[0, 0],
        graycoprops(glcm, "energy")[0, 0],
        graycoprops(glcm, "homogeneity")[0, 0],
    ])


# ==========================================================
# Hu Moments
# ==========================================================

def extract_hu_moments(image):

    return cv2.HuMoments(
        cv2.moments(image)
    ).flatten()


# ==========================================================
# Shape Features
# ==========================================================

def extract_shape_features(image):

    _, binary = cv2.threshold(
        image,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    contours, _ = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:

        return np.zeros(5)

    contour = max(contours, key=cv2.contourArea)

    area = cv2.contourArea(contour)

    perimeter = cv2.arcLength(contour, True)

    circularity = (
        4 * np.pi * area
    ) / (perimeter ** 2 + 1e-6)

    x, y, w, h = cv2.boundingRect(contour)

    aspect_ratio = w / (h + 1e-6)

    hull = cv2.convexHull(contour)

    solidity = area / (
        cv2.contourArea(hull) + 1e-6
    )

    return np.array([
        area,
        perimeter,
        circularity,
        aspect_ratio,
        solidity
    ])


# ==========================================================
# Histogram Features
# ==========================================================

def extract_histogram(image):

    hist = cv2.calcHist(
        [image],
        [0],
        None,
        [32],
        [0, 256]
    ).flatten()

    hist /= hist.sum() + 1e-6

    return hist


# ==========================================================
# Texture Features
# ==========================================================

def extract_texture(image):

    return np.array([
        image.mean(),
        image.std(),
        image.min(),
        image.max()
    ])


# ==========================================================
# Complete Feature Extraction
# ==========================================================

def extract_features(image_path):

    image = preprocess_image(image_path)

    hog_features = extract_hog(image)

    lbp_features = extract_lbp(image)

    glcm_features = extract_glcm(image)

    hu_features = extract_hu_moments(image)

    shape_features = extract_shape_features(image)

    histogram_features = extract_histogram(image)

    texture_features = extract_texture(image)

    feature_vector = np.concatenate([

        hog_features,

        lbp_features,

        glcm_features,

        hu_features,

        shape_features,

        histogram_features,

        texture_features

    ])

    return feature_vector


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    IMAGE = "../dataset/Testing/glioma/Te-gl_1.jpg"

    features = extract_features(IMAGE)

    print("=" * 50)

    print("Feature Extraction Successful")

    print("Total Features :", len(features))

    print(features[:20])

    print("=" * 50)