"""Session 6 student template: Classes and Objects.

In this session, you will refactor the Session 5 functional pipeline
into a class called IrisRuleClassifier. This class bundles configuration
(threshold and labels) and behavior (prediction and evaluation) together.

How to run:
    python3 session6/session6_iris_template.py
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


class IrisRuleClassifier:
    """A class that bundles configuration and prediction/evaluation behavior.

    Configuration (threshold, labels) is stored as attributes on self.
    Behavior (prediction, evaluation) is implemented as methods.
    """

    # Task 1: Define the __init__ Method
    def __init__(self, threshold=2.0):
        """Store configuration inside the object.

        This method runs automatically when you create an IrisRuleClassifier.
        Use self.attribute_name = value to store each item on the object.

        Args:
            threshold (float): The petal_length boundary for classification.
                               Flowers with petal_length below this value
                               are predicted as setosa.
        """
        # Store the threshold as an attribute on self.
        # self.threshold = <your code here>

        # We enforce these attribute names so later sessions can reuse your class.
        # self.positive_label = <your code here>   # should be the string "setosa"
        # self.negative_label = <your code here>   # should be the string "not_setosa"
        pass

    def print_status(self, status_text):
        """Print a small status message in the format: [STATUS] <status_text>.

        This method is provided as a complete example of how to refactor
        a standalone function into a class method.

        Args:
            status_text (str): The message to display.
        """
        print(f"[STATUS] {status_text}")

    # Task 2: Implement compute_threshold_prediction
    def compute_threshold_prediction(self, sample):
        """Predict the label for one flower sample using the threshold rule.

        Compare sample["petal_length"] to self.threshold.
        Return self.positive_label if below the threshold.
        Return self.negative_label otherwise.

        Args:
            sample (dict): One flower sample dictionary with key "petal_length".

        Returns:
            str: self.positive_label or self.negative_label.
        """
        # 1. Read sample["petal_length"]
        # 2. Compare it to self.threshold
        # 3. Return self.positive_label if petal_length < self.threshold
        # 4. Otherwise return self.negative_label
        pass

    # Task 3: Implement derive_true_label
    def derive_true_label(self, sample):
        """Convert the real species name into the lesson label.

        The dataset has three species, but this classifier only uses two
        lesson labels: self.positive_label ("setosa") and
        self.negative_label ("not_setosa").

        This method has one job: return the correct lesson label for one sample.
        It does NOT update any counters.

        Args:
            sample (dict): One flower sample dictionary with key "species".

        Returns:
            str: self.positive_label if species matches, else self.negative_label.
        """
        # If sample["species"] == self.positive_label:
        #     return self.positive_label
        # Otherwise return self.negative_label
        pass

    # Task 4: Implement update_result_counts
    def update_result_counts(self, correct, wrong, total, y_pred_list, y_pred, y_true):
        """Update the counters and prediction list for one sample.

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
        # 1. If y_pred == y_true, increase correct by 1
        # 2. Otherwise increase wrong by 1
        # 3. Always increase total by 1 (even when the prediction is wrong!)
        # 4. Append y_pred to y_pred_list
        # 5. Return the tuple: (correct, wrong, total, y_pred_list)
        pass

    # Task 5: Implement calculate_accuracy
    def calculate_accuracy(self, correct, total):
        """Calculate accuracy as a percentage.

        Args:
            correct (int): Number of correct predictions.
            total (int): Total number of samples processed.

        Returns:
            float: Accuracy percentage between 0.0 and 100.0.
                   Returns 0.0 if total is zero (protect against division by zero).
        """
        # If total > 0:
        #     return (correct / total) * 100
        # Otherwise return 0.0 to avoid dividing by zero
        pass

    # Task 6: Implement run_prediction_loop
    def run_prediction_loop(self, dataset):
        """Run prediction and evaluation on the full dataset.

        This method calls compute_threshold_prediction, derive_true_label,
        and update_result_counts for each sample in the dataset.
        Methods inside the same class can call each other using self.

        Args:
            dataset (list): A list of flower sample dictionaries.

        Returns:
            tuple: (correct, wrong, total, y_pred_list)
        """
        # correct = 0
        # wrong = 0
        # total = 0
        # y_pred_list = []

        # print("\n=== Start Session 6 Prediction Loop ===")

        # for sample in dataset:
        #     y_pred = self.compute_threshold_prediction(<your code here>)
        #     y_true = self.derive_true_label(<your code here>)
        #     correct, wrong, total, y_pred_list = self.update_result_counts(
        #         correct, wrong, total, y_pred_list, y_pred, y_true
        #     )
        #     print(
        #         f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        #         f"petal_length={sample['petal_length']}"
        #     )

        # return correct, wrong, total, y_pred_list
        pass

    # Task 7: Implement print_summary
    def print_summary(self, correct, wrong, total, y_pred_list, accuracy):
        """Print the final results after the prediction loop.

        Args:
            correct (int): Number of correct predictions.
            wrong (int): Number of wrong predictions.
            total (int): Total samples processed.
            y_pred_list (list): All predictions made.
            accuracy (float): Accuracy percentage.
        """
        # print("\n=== Session 6 Summary ===")
        # print("Correct:", <your code here>)
        # print("Wrong:  ", <your code here>)
        # print("Total:  ", <your code here>)
        # print("Accuracy (%):", round(<your code here>, 2))
        # print("All predictions:", <your code here>)
        pass


def main():
    # Task 8: Use the Class in main()

    # Step 1: Load the dataset using the provided setup function
    dataset = setup_application_list()

    # Step 2: Create a classifier object with a chosen threshold
    # classifier = IrisRuleClassifier(<your code here>)

    # Step 3: Print status messages using classifier.print_status(...)
    # classifier.print_status(<your code here>)
    # classifier.print_status(<your code here>)

    # Step 4: Run the prediction loop and unpack the returned tuple
    # correct, wrong, total, y_pred_list = classifier.run_prediction_loop(<your code here>)

    # Step 5: Calculate accuracy from the returned counters
    # accuracy = classifier.calculate_accuracy(<your code here>)

    # Step 6: Print a final status message and the summary
    # classifier.print_status(<your code here>)
    # classifier.print_summary(<your code here>)
    pass


if __name__ == "__main__":
    main()
