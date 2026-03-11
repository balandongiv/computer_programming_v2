"""Session 9 evaluation helpers: train/test split and accuracy scoring using NumPy."""

from typing import Tuple
import numpy as np


def train_test_split(X: np.ndarray, y: np.ndarray, test_size: float = 0.2, seed: int = 1) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """NumPy-only train/test split with shuffling.
    
    Args:
        X: 2D array of features.
        y: 1D array of labels.
        test_size: Proportion of the dataset to include in the test split.
        seed: Random seed for reproducibility.
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    n = X.shape[0]
    rng = np.random.default_rng(seed)
    idx = np.arange(n)
    rng.shuffle(idx)

    test_n = int(n * test_size)
    test_idx = idx[:test_n]
    train_idx = idx[test_n:]

    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]


def accuracy_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Calculate the accuracy of predictions.
    
    Args:
        y_true: 1D array of true labels.
        y_pred: 1D array of predicted labels.
        
    Returns:
        Accuracy as a float between 0.0 and 1.0.
    """
    return float(np.mean(y_true == y_pred))
