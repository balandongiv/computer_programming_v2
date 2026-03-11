"""Session 6 student template: Classes and objects (Refactoring S5 into S6)."""

# Session 6 starter dataset (Iris-only)
dataset = [
    {"id": "flower1", "petal_length": 1.4, "species": "setosa"},
    {"id": "flower2", "petal_length": 1.5, "species": "setosa"},
    {"id": "flower3", "petal_length": 1.3, "species": "setosa"},
    {"id": "flower4", "petal_length": 4.5, "species": "versicolor"},
    {"id": "flower5", "petal_length": 4.7, "species": "versicolor"},
    {"id": "flower6", "petal_length": 5.1, "species": "virginica"},
    {"id": "flower7", "petal_length": 6.0, "species": "virginica"},
]


class IrisRuleClassifier:
    """A class version of our Session 5 function-based classifier.
    
    This class bundles the configuration (threshold, labels) and the behavior
    (predict, evaluate) together.
    """

    def __init__(self, threshold=2.0):
        """Constructor: Sets up the object's data (attributes).
        
        Args:
            threshold (float): The petal_length threshold for classification.
        """
        # TODO 1: Store threshold as an object attribute
        self.threshold = threshold
        # We enforce these attribute names so that later sessions can use your class without changes.
        self.positive_label = "setosa"
        self.negative_label = "not_setosa"

    def predict(self, sample):
        """Predict 'setosa' or 'not_setosa' for a single sample.
        
        Args:
            sample (dict): A dictionary representing one flower.
            
        Returns:
            str: "setosa" or "not_setosa".
        """
        # TODO 2: Re-implement the threshold logic here.
        # Remember: use self.threshold instead of settings['threshold']
        # Be careful not to omit `self` when accessing attributes!
        if sample["petal_length"] < self.threshold:
            return self.positive_label
        return self.negative_label

    def evaluate(self, dataset):
        """Evaluate the classifier on a full dataset and return accuracy.
        
        Args:
            dataset (list): A list of flower dictionaries.
            
        Returns:
            float: Accuracy between 0.0 and 1.0.
        """
        correct = 0
        total = 0

        # TODO 3: Implement the evaluation loop
        # Loop through each sample, get a prediction using self.predict(sample),
        # determine the true binary label, and update correct/total.
        # IMPORTANT: ensure `total` increments for every sample.
        for sample in dataset:
            prediction = self.predict(sample)
            truth = self.positive_label if sample["species"] == "setosa" else self.negative_label
            
            if prediction == truth:
                correct += 1
            total += 1

        return correct / total if total > 0 else 0.0


# --- Self-Check / Testing Block ---
def _test_evaluate_logic():
    """Verify that evaluate correctly increments total for all samples."""
    test_data = [
        {"petal_length": 1.5, "species": "setosa"}, # True pos
        {"petal_length": 1.5, "species": "versicolor"} # False pos
    ]
    clf = IrisRuleClassifier(threshold=2.0)
    acc = clf.evaluate(test_data)
    assert acc == 0.5, f"Expected accuracy 0.5, got {acc}. Did you forget to increment total for wrong predictions?"
    print("[Self-Check Passed] evaluate increments total correctly.")


def main():
    print("=== Student Label ===")
    student_id = "YOUR_ID_HERE"
    full_name = "YOUR_FULL_NAME_HERE"
    print("Student ID:", student_id)
    print("Full Name:", full_name)

    # TODO 4: Create a classifier object
    my_clf = IrisRuleClassifier()  # Default threshold 2.0
    print("\nCreated Classifier with threshold:", my_clf.threshold)

    # TODO 5: Evaluate it
    accuracy = my_clf.evaluate(dataset)
    print("Accuracy (Default):", accuracy)

    # TODO 6: Create customized classifiers and compare
    clf_strict = IrisRuleClassifier(threshold=1.5)
    clf_loose = IrisRuleClassifier(threshold=2.5)

    print("\nAccuracy (Strict 1.5):", clf_strict.evaluate(dataset))
    print("Accuracy (Loose 2.5):", clf_loose.evaluate(dataset))


if __name__ == "__main__":
    _test_evaluate_logic()
    main()
