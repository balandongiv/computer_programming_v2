"""Session 7 student template: Inheritance and Polymorphism.

This file defines a base classifier with shared evaluation logic, and multiple child
classes that implement different prediction rules. This demonstrates how inheritance
reduces code duplication and how polymorphism allows different classifiers to be used interchangeably.
"""

import random

# A small built-in dataset (list of dictionaries)
dataset = [
    {"id": "flower1", "petal_length": 1.4, "species": "setosa"},
    {"id": "flower2", "petal_length": 1.5, "species": "setosa"},
    {"id": "flower3", "petal_length": 1.3, "species": "setosa"},
    {"id": "flower4", "petal_length": 4.5, "species": "versicolor"},
    {"id": "flower5", "petal_length": 4.7, "species": "versicolor"},
    {"id": "flower6", "petal_length": 5.1, "species": "virginica"},
    {"id": "flower7", "petal_length": 6.0, "species": "virginica"},
]


class ClassifierBase:
    """Base class holding shared logic (evaluation loop).
    
    This class should not be instantiated directly.
    """

    def __init__(self):
        # We don't store threshold here anymore, because not all classifiers use a threshold!
        pass

    def predict(self, sample):
        """Predict the label for a single sample.
        
        Must be overridden by child classes.
        """
        # TODO 1: Raise NotImplementedError to force child classes to write their own
        raise NotImplementedError("Child class must implement predict()")

    def evaluate(self, dataset):
        """Evaluate the classifier on a full dataset.
        
        Args:
            dataset (list): A list of flower sample dictionaries.
            
        Returns:
            float: Accuracy of the classifier.
        """
        # TODO 2: Reuse the evaluate logic from Session 6
        # Key change: it calls self.predict(), which the child provides
        correct = 0
        total = 0

        for sample in dataset:
            prediction = self.predict(sample)
            truth = "setosa" if sample["species"] == "setosa" else "not_setosa"
            
            if prediction == truth:
                correct += 1
            
            # BUG FIX: total must increment for every sample, not just correct ones!
            total += 1

        return correct / total if total > 0 else 0.0


class RuleClassifier(ClassifierBase):
    """Child class: Session 6 rule logic wrapped in inheritance."""

    def __init__(self, threshold=2.0):
        super().__init__()  # Good practice to initialize parent
        self.threshold = threshold

    def predict(self, sample):
        """Predict label using a simple threshold rule."""
        # TODO 3: Implement the familiar rule logic
        if sample["petal_length"] < self.threshold:
            return "setosa"
        return "not_setosa"


class NearestCentroidClassifier(ClassifierBase):
    """Child class: Classifies by finding the closest target value."""

    def __init__(self, setosa_target=1.4, non_setosa_target=4.5):
        super().__init__()
        self.setosa_target = setosa_target
        self.non_setosa_target = non_setosa_target

    def predict(self, sample):
        """Predict label by computing distance to centroids."""
        # TODO 4: Calculate distance to both targets
        val = sample["petal_length"]
        dist_setosa = abs(val - self.setosa_target)
        dist_non = abs(val - self.non_setosa_target)

        if dist_setosa < dist_non:
            return "setosa"
        return "not_setosa"


class RandomGuessClassifier(ClassifierBase):
    """Child class: A classifier that randomly guesses the label (optional exercise)."""
    
    def __init__(self):
        super().__init__()
        
    def predict(self, sample):
        """Predict randomly."""
        return random.choice(["setosa", "not_setosa"])


def main():
    print("=== Student Label ===")
    student_id = "YOUR_ID_HERE"
    full_name = "YOUR_FULL_NAME_HERE"
    print("Student ID:", student_id)
    print("Full Name:", full_name)

    # TODO 5: Create objects for all types
    classifiers = [
        RuleClassifier(threshold=2.0),
        NearestCentroidClassifier(),
        RandomGuessClassifier()
    ]

    # TODO 6: Evaluate them using polymorphism
    # Note: They all use the same .evaluate() method inherited from ClassifierBase!
    print("\n=== Model Comparison ===")
    for clf in classifiers:
        acc = clf.evaluate(dataset)
        print(f"{clf.__class__.__name__}: Accuracy = {acc}")


if __name__ == "__main__":
    main()
