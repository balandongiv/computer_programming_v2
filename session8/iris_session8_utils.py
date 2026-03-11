"""Session 8 shared utilities: Iris data loading, NumPy conversion, masks, and centroids."""

import os
from typing import Tuple, Dict
import numpy as np


FEATURE_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width"]


def get_builtin_dataset() -> list:
    """Return a small built-in Iris dataset for reproducible labs."""
    return [
        {"id": "flower1", "sepal_length": 5.1, "sepal_width": 3.5,
            "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"},
        {"id": "flower2", "sepal_length": 4.9, "sepal_width": 3.0,
            "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"},
        {"id": "flower3", "sepal_length": 5.4, "sepal_width": 3.9,
            "petal_length": 1.7, "petal_width": 0.4, "species": "setosa"},
        {"id": "flower4", "sepal_length": 5.0, "sepal_width": 3.4,
            "petal_length": 1.5, "petal_width": 0.2, "species": "setosa"},
        {"id": "flower5", "sepal_length": 7.0, "sepal_width": 3.2,
            "petal_length": 4.7, "petal_width": 1.4, "species": "versicolor"},
        {"id": "flower6", "sepal_length": 6.4, "sepal_width": 3.2,
            "petal_length": 4.5, "petal_width": 1.5, "species": "versicolor"},
        {"id": "flower7", "sepal_length": 6.3, "sepal_width": 3.3,
            "petal_length": 6.0, "petal_width": 2.5, "species": "virginica"},
        {"id": "flower8", "sepal_length": 5.8, "sepal_width": 2.7,
            "petal_length": 5.1, "petal_width": 1.9, "species": "virginica"},
        {"id": "flower9", "sepal_length": 6.1, "sepal_width": 2.8,
            "petal_length": 4.0, "petal_width": 1.3, "species": "versicolor"},
        {"id": "flower10", "sepal_length": 5.7, "sepal_width": 2.8,
            "petal_length": 4.1, "petal_width": 1.3, "species": "versicolor"},
        {"id": "flower11", "sepal_length": 5.2, "sepal_width": 2.7,
            "petal_length": 1.9, "petal_width": 0.5, "species": "versicolor"},
        {"id": "flower12", "sepal_length": 5.1, "sepal_width": 3.8,
            "petal_length": 1.6, "petal_width": 0.2, "species": "setosa"},
    ]


def dataset_to_numpy(dataset: list) -> Tuple[np.ndarray, np.ndarray]:
    """Convert list-of-dicts dataset into NumPy features and labels.
    
    Args:
        dataset: A list of dictionaries representing flowers.
        
    Returns:
        X: 2D array of features.
        y: 1D array of labels.
    """
    X = np.array([[row[name] for name in FEATURE_NAMES]
                 for row in dataset], dtype=float)
    y = np.array([row["species"] for row in dataset], dtype=str)
    return X, y


def load_iris_csv(filepath: str = "iris.csv", skip_header: int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """Load iris CSV into NumPy arrays; fallback to built-in data if file missing.
    
    Args:
        filepath: Path to the CSV file.
        skip_header: Number of lines to skip at the beginning of the file.
        
    Returns:
        Tuple containing:
            X (np.ndarray): 2D array of shape (n_samples, 4) with feature values.
            y (np.ndarray): 1D array of shape (n_samples,) with string labels.
    """
    if not os.path.exists(filepath):
        print(f"[ERROR] Could not find {filepath}. Falling back to built-in dataset.")
        return dataset_to_numpy(get_builtin_dataset())

    raw = np.genfromtxt(
        filepath,
        delimiter=",",
        dtype=None,          # allow mixed dtype (numbers + strings)
        encoding="utf-8",
        skip_header=skip_header,
    )

    if raw.size == 0:
        return dataset_to_numpy(get_builtin_dataset())

    if raw.ndim == 1:
        raw = raw.reshape(1, -1)

    X = np.column_stack([raw[i] for i in range(4)]).astype(float)
    y = np.array(raw[4], dtype=str)
    return X, y


def class_counts(y: np.ndarray) -> Dict[str, int]:
    """Return class counts as a dictionary.
    
    Args:
        y: 1D array of labels.
        
    Returns:
        A dictionary mapping label strings to their integer counts.
    """
    labels, counts = np.unique(y, return_counts=True)
    return {labels[i]: int(counts[i]) for i in range(len(labels))}


def compute_class_centroids(X: np.ndarray, y: np.ndarray) -> Dict[str, np.ndarray]:
    """Compute centroid per class using np.mean(..., axis=0).
    
    Args:
        X: 2D array of features.
        y: 1D array of labels.
        
    Returns:
        A dictionary mapping each label string to its 1D centroid vector.
    """
    centroids = {}
    for label in np.unique(y):
        mask = (y == label)
        centroids[label] = np.mean(X[mask], axis=0)
    return centroids


def boolean_mask_for_label(y: np.ndarray, label: str) -> np.ndarray:
    """Return boolean mask selecting rows for one label.
    
    Args:
        y: 1D array of labels.
        label: The string label to match.
        
    Returns:
        A 1D boolean array where True indicates a match.
    """
    return y == label
