"""Session 8 shared models: session 7-compatible classifier interface with NumPy internals."""

import numpy as np

try:
    from session8.iris_session8_utils import compute_class_centroids
except ModuleNotFoundError:
    from iris_session8_utils import compute_class_centroids


class ClassifierBase:
    """Base class preserving session 7 method interface."""

    def __init__(self):
        self.model_name = self.__class__.__name__

    def fit(self, X: np.ndarray, y: np.ndarray):
        """Fit the model to the training data.
        
        Args:
            X: 2D array of features.
            y: 1D array of labels.
            
        Returns:
            self
        """
        return self

    def predict_one(self, sample: np.ndarray):
        """Predict label for a single sample."""
        raise NotImplementedError("Child class must implement predict_one().")

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict labels for an array of samples."""
        return np.array([self.predict_one(row) for row in X], dtype=str)

    def predict_all(self, X: np.ndarray) -> np.ndarray:
        """Alias for predict."""
        return self.predict(X)

    def evaluate(self, X: np.ndarray, y: np.ndarray) -> dict:
        """Evaluate accuracy of the model on provided data.
        
        Args:
            X: 2D array of features.
            y: 1D array of labels.
            
        Returns:
            Dictionary with evaluation metrics (correct, wrong, total, accuracy).
        """
        y_pred = self.predict_all(X)
        correct = int(np.sum(y == y_pred))
        total = int(y.shape[0])
        wrong = total - correct
        accuracy = (correct / total) * 100 if total > 0 else 0.0
        return {
            "correct": correct,
            "wrong": wrong,
            "total": total,
            "accuracy": accuracy,
            "y_pred": y_pred,
        }


class NumpyCentroidClassifier(ClassifierBase):
    """Centroid classifier using NumPy arrays and selectable distance metric."""

    def __init__(self, metric="l2"):
        """Initialize classifier with distance metric ('l1' or 'l2')."""
        super().__init__()
        self.metric = metric
        self.centroids = {}
        self.classes_ = np.array([], dtype=str)

    def fit(self, X: np.ndarray, y: np.ndarray):
        """Compute and store class centroids."""
        super().fit(X, y)
        self.centroids = compute_class_centroids(X, y)
        self.classes_ = np.array(sorted(self.centroids.keys()), dtype=str)
        return self

    def _distance(self, a: np.ndarray, b: np.ndarray) -> float:
        """Compute distance between two vectors."""
        if self.metric == "l2":
            return float(np.sqrt(np.sum((a - b) ** 2)))
        if self.metric == "l1":
            return float(np.sum(np.abs(a - b)))
        raise ValueError("metric must be 'l2' or 'l1'")

    def predict_one(self, sample: np.ndarray) -> str:
        """Predict the class of a single sample by finding the nearest centroid."""
        best_label = None
        best_dist = None

        for label in self.classes_:
            dist = self._distance(sample, self.centroids[label])
            if (best_dist is None) or (dist < best_dist):
                best_dist = dist
                best_label = label

        return best_label
