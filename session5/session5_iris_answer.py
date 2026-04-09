"""Session 5: Positional and keyword arguments with the iris classifier.

This session keeps the same classifier idea from Session 4.
The new goal is to control the same pipeline with default values,
positional arguments, and keyword arguments.
"""

POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"


def make_print_status(status_text):
    """Print a small status message."""
    print(f"[STATUS] {status_text}")


def setup_application_list():
    """Return the dataset as a list of flower dictionaries.

    This helper is provided for you. Do not modify it.
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


# Task 1: Refactor calculate_accuracy to use keyword-friendly defaults
def calculate_accuracy(correct=0, total=0):
    """Calculate the accuracy percentage."""
    if total > 0:
        accuracy = (correct / total) * 100
    else:
        accuracy = 0.0

    return accuracy


def compute_threshold_prediction(sample, threshold):
    """Predict the label for one flower sample using the threshold rule."""
    if sample["petal_length"] < threshold:
        return POSITIVE_LABEL
    return NEGATIVE_LABEL


def derive_true_label(sample):
    """Convert the real species into the lesson label."""
    if sample["species"] == POSITIVE_LABEL:
        return POSITIVE_LABEL
    return NEGATIVE_LABEL


# Task 2: Rename setup_application to run_classifier_pipeline
def run_classifier_pipeline(threshold=2.0, print_each=True):
    """Run the full classifier pipeline and compute accuracy."""
    dataset = setup_application_list()
    correct, wrong, total, y_pred_list = run_prediction_loop(
        dataset,
        threshold=threshold,
        print_each=print_each,
    )
    accuracy = calculate_accuracy(
        correct=correct,
        total=total,
    )
    return correct, wrong, total, y_pred_list, accuracy


# Task 3: Refactor run_prediction_loop to combine positional and keyword arguments
def run_prediction_loop(dataset, threshold=2.0, print_each=True):
    """Run the prediction loop with the chosen threshold."""
    correct = 0
    wrong = 0
    total = 0
    y_pred_list = []

    print("\n=== Start Session 5 Prediction Loop ===")

    for sample in dataset:
        y_pred = compute_threshold_prediction(sample, threshold)
        y_true = derive_true_label(sample)
        correct, wrong, total, y_pred_list = update_result_counts(
            correct,
            wrong,
            total,
            y_pred_list,
            y_pred=y_pred,
            y_true=y_true,
        )

        if print_each:
            print(
                f"id={sample['id']} | true={y_true} | pred={y_pred} | "
                f"petal_length={sample['petal_length']}"
            )

    return correct, wrong, total, y_pred_list


# Task 4: Use update_result_counts with combined positional and keyword arguments
def update_result_counts(correct, wrong, total, y_pred_list, y_pred, y_true):
    """Update the counters and prediction list for one sample."""
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1

    total += 1
    y_pred_list.append(y_pred)

    return correct, wrong, total, y_pred_list


def print_summary(correct, wrong, total, y_pred_list, accuracy):
    """Print the final results after the loop is finished."""
    print("\n=== Session 5 Summary ===")
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Total:", total)
    print("Accuracy (%):", round(accuracy, 2))
    print("All predictions:", y_pred_list)


def main():
    """Run the Session 5 experiments."""

    # Task 5: Add the default run in main()
    make_print_status("Default run")
    correct, wrong, total, y_pred_list, accuracy = run_classifier_pipeline()
    print_summary(correct, wrong, total, y_pred_list, accuracy)

    # Task 6: Add the positional override run in main()
    make_print_status("Positional override run")
    correct, wrong, total, y_pred_list, accuracy = run_classifier_pipeline(1.8, False)
    print_summary(correct, wrong, total, y_pred_list, accuracy)

    # Task 7: Add the keyword override run in main()
    make_print_status("Keyword override run")
    correct, wrong, total, y_pred_list, accuracy = run_classifier_pipeline(
        threshold=1.8,
        print_each=False,
    )
    print_summary(correct, wrong, total, y_pred_list, accuracy)

    # Task 8: Add the reordered keyword run in main()
    make_print_status("Reordered keyword run")
    correct, wrong, total, y_pred_list, accuracy = run_classifier_pipeline(
        print_each=False,
        threshold=1.8,
    )
    print_summary(correct, wrong, total, y_pred_list, accuracy)


if __name__ == "__main__":
    main()
