"""Session 4: Move Session 3 code into functions.

This version keeps the same rule from Session 3.
The goal is to help a beginner see where each part came from.
We keep the code simple and close to the original step-by-step style.
"""
LABEL_KEY = "species"
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"


def make_print_status(status_text):
    """Print a small status message.

    Args:
        status_text (str): A short message to show what the program is doing.
    """
    print(f"[STATUS] {status_text}")


def compute_threshold_prediction(sample):
    """Predict the label for one flower sample.

    This uses the same rule from Session 3:
    if petal_length is less than 2.0, predict "setosa".
    Otherwise, predict "not_setosa".

    Args:
        sample (dict): One flower sample.

    Returns:
        str: The predicted label.
    """

    if sample[FEATURE_NAME] < THRESHOLD:
        y_pred = POSITIVE_LABEL
    else:
        y_pred = NEGATIVE_LABEL

    return y_pred


def derive_true_label(sample):
    """Convert the real species into the lesson label.

    In this lesson, we only use two labels:
    - "setosa"
    - "not_setosa"

    Args:
        sample (dict): One flower sample.

    Returns:
        str: The true label for this lesson.
    """

    if sample[LABEL_KEY] == POSITIVE_LABEL:
        y_true = POSITIVE_LABEL
    else:
        y_true = NEGATIVE_LABEL

    return y_true


def update_result_counts(correct, wrong, total, y_pred_list, y_pred, y_true):
    """Update the counters and prediction list for one sample.

    Args:
        correct (int): Current number of correct predictions.
        wrong (int): Current number of wrong predictions.
        total (int): Current number of processed samples.
        y_pred_list (list): Current list of predictions.
        y_pred (str): Predicted label.
        y_true (str): True label.

    Returns:
        tuple: Updated correct, wrong, total, y_pred_list
    """
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1

    total += 1
    y_pred_list.append(y_pred)

    return correct, wrong, total, y_pred_list


def calculate_accuracy(correct, total):
    """Calculate accuracy percentage.

    Args:
        correct (int): Number of correct predictions.
        total (int): Number of processed samples.

    Returns:
        float: Accuracy percentage.
    """
    if total > 0:
        accuracy = (correct / total) * 100
    else:
        accuracy = 0.0

    return accuracy


def run_prediction_loop(dataset):
    """Run the same prediction loop from Session 3, but inside a function.

    This function keeps the beginner-friendly variables:
    correct, wrong, total, and y_pred_list.

    Args:
        dataset (list): A list of flower dictionaries.

    Returns:
        tuple: correct, wrong, total, y_pred_list, accuracy
    """
    # Task 3 from Session 3: initialize metrics and predictions
    correct = 0      # Count of correct predictions
    wrong = 0        # Count of wrong predictions
    total = 0        # Total samples processed
    y_pred_list = []  # List of all predictions made

    print("\n=== Start session 4 Prediction Loop ===")

    # Task 4 and Task 5 from Session 3
    for sample in dataset:
        # 1. Compute prediction
        y_pred = compute_threshold_prediction(sample)

        # 2. Derive true label
        y_true = derive_true_label(sample)

        # 3. Update counters and prediction list
        correct, wrong, total, y_pred_list = update_result_counts(
            correct, wrong, total, y_pred_list, y_pred, y_true
        )

        # 4. Print one line for this sample
        print(
            f"id={sample['id']} | true={y_true} | pred={y_pred} | "
            f"petal_length={sample['petal_length']}"
        )

    return correct, wrong, total, y_pred_list


def print_summary(correct, wrong, total, y_pred_list, accuracy):
    """Print the final results after the loop is finished.

    Args:
        correct (int): Number of correct predictions.
        wrong (int): Number of wrong predictions.
        total (int): Number of processed samples.
        y_pred_list (list): List of predicted labels.
        accuracy (float): Accuracy percentage.
    """
    print("\n=== session 4 Summary ===")
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Total:", total)
    print("Accuracy (%):", round(accuracy, 2))
    print("All predictions:", y_pred_list)


def setup_application_list():
    """Combination of Task 1 and Task 2 in session 3, but now in a function."""
    # Task 1 in session 3: Define dictionaries for flower1 and flower2 using canonical keys

    flower1 = {
        "id": "flower1",
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }

    flower2 = {
        "id": "flower2",
        "sepal_length": 4.9,
        "sepal_width": 3.0,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }

    # Task 2 in session 3: Build the dataset list
    # Combine our dictionaries into a single list
    dataset = [flower1, flower2]
    return dataset


def main():
    """Run the full beginner version of the program."""
    make_print_status("Build dataset")
    dataset = setup_application_list()

    make_print_status("Run prediction loop")
    correct, wrong, total, y_pred_list = run_prediction_loop(dataset)
    accuracy = calculate_accuracy(correct, total)

    make_print_status("Print summary")
    print_summary(correct, wrong, total, y_pred_list, accuracy)


if __name__ == "__main__":
    main()
