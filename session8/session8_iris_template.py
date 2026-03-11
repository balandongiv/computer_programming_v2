"""Session 8 student template: NumPy arrays, centroids, masks, and imports."""

import os
import sys

import numpy as np

# Ensure the root directory is in sys.path so imports work correctly
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from session8.iris_session8_utils import (
    boolean_mask_for_label,
    class_counts,
    compute_class_centroids,
    load_iris_csv,
)
from session8.iris_session8_models import NumpyCentroidClassifier


def main():
    print("=== Student Label ===")
    student_id = "YOUR_ID_HERE"
    full_name = "YOUR_FULL_NAME_HERE"
    print("Student ID:", student_id)
    print("Full Name:", full_name)

    # Load X and y from CSV (or built-in fallback)
    X, y = load_iris_csv("iris.csv", skip_header=1)

    print("\n=== Array Overview ===")
    print("X shape:", X.shape)
    print("X dtype:", X.dtype)
    print("y shape:", y.shape)
    print("y dtype:", y.dtype)

    print("\n=== Indexing and Slicing ===")
    print("First row:", X[0])
    print("Last row:", X[-1])
    print("First 5 rows:\n", X[:5])
    # Select rows 0 to end, columns 2 to 3 (petal length and width)
    print("Petal matrix shape (cols 2:4):", X[:, 2:4].shape)
    print("First 10 labels:", y[:10])

    print("\n=== Class Counts ===")
    counts = class_counts(y)
    for label, count in counts.items():
        print(label, "->", count)

    print("\n=== Class Centroids ===")
    centroids = compute_class_centroids(X, y)
    for label in sorted(centroids.keys()):
        print(label, "->", np.round(centroids[label], 2))

    # Axis 0 vs Axis 1 explanation
    # axis=0 computes the mean across rows (per column), giving a centroid vector.
    # axis=1 computes the mean across columns (per row), giving a mean value per sample.

    print("\n=== Classifier Interface Reuse (from session 7) ===")
    model = NumpyCentroidClassifier(metric="l2")
    model.fit(X, y)
    result = model.evaluate(X, y)
    print("Correct:", result["correct"])
    print("Wrong:", result["wrong"])
    print("Total:", result["total"])
    print("Accuracy (%):", round(result["accuracy"], 2))

    print("\n=== Metric Comparison (l2 vs l1) ===")
    for metric in ["l2", "l1"]:
        metric_model = NumpyCentroidClassifier(metric=metric)
        metric_model.fit(X, y)
        metric_result = metric_model.evaluate(X, y)
        print(metric, "accuracy (%):", round(metric_result["accuracy"], 2))

    # --- Reflection on LLM Usage ---
    # One thing the LLM explained clearly:
    # (Write your reflection here)
    # 
    # One thing I still find confusing:
    # (Write your reflection here)


if __name__ == "__main__":
    main()
