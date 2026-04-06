"""Session 7 complete answer: Inheritance and Polymorphism.

This file shows the complete solution after all tasks are finished.
Students should arrive at this implementation after completing Tasks 1-10.

How to run:
    python3 session7/session7_iris_answer.py
"""


def setup_application_list():
    """Return the dataset as a list of flower dictionaries.

    This function is provided for you. Do not modify it.
    """
    return [
        {"id": "flower1", "petal_length": 1.4, "species": "setosa"},
        {"id": "flower2", "petal_length": 1.5, "species": "setosa"},
        {"id": "flower3", "petal_length": 1.3, "species": "setosa"},
        {"id": "flower4", "petal_length": 4.5, "species": "versicolor"},
        {"id": "flower5", "petal_length": 4.7, "species": "versicolor"},
        {"id": "flower6", "petal_length": 5.1, "species": "virginica"},
        {"id": "flower7", "petal_length": 6.0, "species": "virginica"},
    ]


class ClassifierBase:
    """Parent class holding shared evaluation logic.

    This class is not meant to be used directly.
    Child classes must provide their own predict() method.
    All other evaluation methods are inherited from this class.
    """

    def __init__(self):
        # Store the two lesson labels. All child classes inherit these.
        self.positive_label = "setosa"
        self.negative_label = "not_setosa"

    def predict(self, sample):
        """Child classes must provide their own version of this method.

        This line is already provided. Do not change it.
        If a child class does not override predict(), this error will appear
        to remind the student to implement it.
        """
        raise NotImplementedError("Child class must implement predict()")

    # Task 1: Implement derive_true_label
    def derive_true_label(self, sample):
        """Convert the raw species name into the lesson label.

        The dataset has three species, but this classifier only uses two
        lesson labels: self.positive_label ("setosa") and
        self.negative_label ("not_setosa").

        Args:
            sample (dict): One flower sample dictionary with key "species".

        Returns:
            str: self.positive_label if species matches, else self.negative_label.
        """
        if sample["species"] == self.positive_label:
            return self.positive_label
        return self.negative_label

    # Task 2: Implement update_result_counts
    def update_result_counts(self, correct, wrong, total, y_pred_list, y_pred, y_true):
        """Update counters and prediction list for one sample.

        Compare y_pred to y_true and update the appropriate counter.
        Always increment total, even when the prediction is wrong.

        Args:
            correct (int): Number of correct predictions so far.
            wrong (int): Number of wrong predictions so far.
            total (int): Total samples processed so far.
            y_pred_list (list): List of all predictions made so far.
            y_pred (str): The prediction for the current sample.
            y_true (str): The true label for the current sample.

        Returns:
            tuple: Updated (correct, wrong, total, y_pred_list).
        """
        if y_pred == y_true:
            correct += 1
        else:
            wrong += 1

        total += 1
        y_pred_list.append(y_pred)

        return correct, wrong, total, y_pred_list

    # Task 3: Implement calculate_accuracy
    def calculate_accuracy(self, correct, total):
        """Calculate accuracy as a percentage.

        Args:
            correct (int): Number of correct predictions.
            total (int): Total number of samples processed.

        Returns:
            float: Accuracy percentage between 0.0 and 100.0.
                   Returns 0.0 if total is zero (protection against division by zero).
        """
        if total > 0:
            return (correct / total) * 100
        return 0.0

    # Task 4: Implement evaluate
    def evaluate(self, dataset):
        """Shared evaluation loop for all classifiers.

        This method calls self.predict(sample) for each sample in the dataset.
        Because predict() is overridden in each child class, the correct
        child-specific prediction rule is used automatically.

        This is the key benefit of inheritance: one evaluate() method works
        for every classifier type.

        Args:
            dataset (list): A list of flower sample dictionaries.

        Returns:
            tuple: (correct, wrong, total, y_pred_list, accuracy)
        """
        correct = 0
        wrong = 0
        total = 0
        y_pred_list = []

        print("\n=== Start Evaluation ===")

        for sample in dataset:
            y_pred = self.predict(sample)
            y_true = self.derive_true_label(sample)
            correct, wrong, total, y_pred_list = self.update_result_counts(
                correct, wrong, total, y_pred_list, y_pred, y_true
            )
            print(
                f"id={sample['id']} | true={y_true} | pred={y_pred} | "
                f"petal_length={sample['petal_length']}"
            )

        accuracy = self.calculate_accuracy(correct, total)
        return correct, wrong, total, y_pred_list, accuracy


class RuleClassifier(ClassifierBase):
    """Child class: classifies flowers using a threshold on petal_length.

    This class inherits evaluate(), derive_true_label(), update_result_counts(),
    and calculate_accuracy() from ClassifierBase.
    It only needs to provide __init__ and predict().
    """

    # Task 5: Define RuleClassifier.__init__
    def __init__(self, threshold=2.0):
        """Initialise the rule classifier.

        Call the parent __init__ first using super().__init__().
        Then store the threshold on self.

        Args:
            threshold (float): The petal_length boundary for classification.
        """
        super().__init__()
        self.threshold = threshold

    # Task 6: Implement RuleClassifier.predict
    def predict(self, sample):
        """Predict using the threshold rule.

        If petal_length is below the threshold, predict positive_label.
        Otherwise predict negative_label.

        Args:
            sample (dict): One flower sample dictionary with key "petal_length".

        Returns:
            str: self.positive_label or self.negative_label.
        """
        if sample["petal_length"] < self.threshold:
            return self.positive_label
        return self.negative_label


class NearestCentroidClassifier(ClassifierBase):
    """Child class: classifies flowers by distance to two centroid values.

    This class inherits evaluate(), derive_true_label(), update_result_counts(),
    and calculate_accuracy() from ClassifierBase.
    It only needs to provide __init__ and predict().
    """

    # Task 7: Define NearestCentroidClassifier.__init__
    def __init__(self, setosa_center=1.5, not_setosa_center=4.5):
        """Initialise the nearest centroid classifier.

        Call the parent __init__ first using super().__init__().
        Then store both centroid values on self.

        Args:
            setosa_center (float): Typical petal_length for setosa flowers.
            not_setosa_center (float): Typical petal_length for non-setosa flowers.
        """
        super().__init__()
        self.setosa_center = setosa_center
        self.not_setosa_center = not_setosa_center

    # Task 8: Implement NearestCentroidClassifier.predict
    def predict(self, sample):
        """Predict by choosing the closer centroid.

        Use abs() to compute the distance between petal_length and each center.
        Return the label whose center is closer.

        abs(x) returns the absolute value of x (the distance from zero).
        For example: abs(1.4 - 1.5) = 0.1, abs(1.4 - 4.5) = 3.1

        Args:
            sample (dict): One flower sample dictionary with key "petal_length".

        Returns:
            str: self.positive_label or self.negative_label.
        """
        petal_length = sample["petal_length"]
        dist_to_setosa = abs(petal_length - self.setosa_center)
        dist_to_not_setosa = abs(petal_length - self.not_setosa_center)

        if dist_to_setosa < dist_to_not_setosa:
            return self.positive_label
        return self.negative_label


# Task 9: Implement run_and_report
def run_and_report(classifier, dataset, name):
    """Run evaluation for any classifier and print a short summary.

    This function accepts any classifier object that has an evaluate() method.
    It does not care whether the classifier is a RuleClassifier,
    NearestCentroidClassifier, or any other classifier type.
    This is polymorphism: different objects used through the same interface.

    Args:
        classifier: Any object with an evaluate(dataset) method.
        dataset (list): A list of flower sample dictionaries.
        name (str): A label to identify this classifier in the output.
    """
    print(f"\n--- {name} ---")
    correct, wrong, total, y_pred_list, accuracy = classifier.evaluate(dataset)
    print(f"Correct: {correct}  Wrong: {wrong}  Total: {total}")
    print(f"Accuracy (%): {round(accuracy, 2)}")


def main():
    # Task 10: Compare Classifiers in main()

    # Step 1: Load the dataset
    dataset = setup_application_list()

    # Step 2: Create a RuleClassifier and a NearestCentroidClassifier
    rule_clf = RuleClassifier(threshold=2.0)
    centroid_clf = NearestCentroidClassifier(
        setosa_center=1.5, not_setosa_center=4.5)

    # Step 3: Call run_and_report for each classifier
    run_and_report(rule_clf, dataset, "RuleClassifier")
    run_and_report(centroid_clf, dataset, "NearestCentroidClassifier")

    # Step 4: Demonstrate polymorphism using a loop over a list of classifiers
    print("\n\n=== Polymorphism Demo: Loop Over Multiple Classifiers ===")
    classifiers = [
        RuleClassifier(threshold=2.0),
        NearestCentroidClassifier(setosa_center=1.5, not_setosa_center=4.5),
    ]
    for clf in classifiers:
        run_and_report(clf, dataset, clf.__class__.__name__)


if __name__ == "__main__":
    main()
