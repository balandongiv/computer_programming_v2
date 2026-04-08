"""Session 5: Positional and keyword arguments with the iris classifier.

This session keeps the same classifier idea from Session 4.
The new goal is to make the pipeline easier to control from function calls.
"""

import csv

from helper.iris_utils import fit_threshold_from_setosa

DEFAULT_IRIS_FILE = "session5/iris_data.csv"


def make_print_status(status_text):
    """Print a small status message."""
    print(f"[STATUS] {status_text}")


# Task 1: Refactor calculate_accuracy to use keyword-friendly defaults

def calculate_accuracy(correct=0, total=0):
    """Calculate the accuracy percentage."""
    if total > 0:
        accuracy = (correct / total) * 100
    else:
        accuracy = 0.0

    return accuracy


# Task 2: Build the keyword-friendly setup_application function

def setup_application(filepath=None, threshold=None, print_each=True, use_fit=False):
    """Set up the dataset, settings, metrics, and accuracy for one run.

    Args:
        filepath (str | None): CSV path. Defaults to session5/iris_data.csv.
        threshold (float | None): Manual threshold override.
        print_each (bool): Whether to print one line per sample.
        use_fit (bool): Whether to learn the threshold from the dataset.

    Returns:
        tuple: settings, dataset, metrics, accuracy
    """
    if filepath is None:
        filepath = DEFAULT_IRIS_FILE

    dataset = load_iris_data(filepath)
    settings = get_default_settings()

    if use_fit:
        settings["threshold"] = fit_threshold_from_setosa(dataset, settings)
    elif threshold is not None:
        settings["threshold"] = threshold

    metrics = initialize_predictions(dataset, settings, print_each)
    accuracy = calculate_accuracy(
        correct=metrics["correct"],
        total=metrics["total"],
    )
    return settings, dataset, metrics, accuracy


def get_default_settings():
    """Return the default classifier settings for this lesson."""
    return {
        "label_key": "species",
        "threshold": 2.0,
        "feature_name": "petal_length",
        "positive_label": "setosa",
        "negative_label": "not_setosa",
    }


def load_iris_data(filepath):
    """Load the iris dataset from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        list: A list of flower dictionaries.
    """
    dataset = []
    with open(filepath, "r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            sample = {
                "id": row["id"],
                "sepal_length": float(row["sepal_length"]),
                "sepal_width": float(row["sepal_width"]),
                "petal_length": float(row["petal_length"]),
                "petal_width": float(row["petal_width"]),
                "species": row["species"],
            }
            dataset.append(sample)

    return dataset


def determine_binary_label(sample, settings):
    """Predict a binary label using the threshold rule."""
    if sample[settings["feature_name"]] < settings["threshold"]:
        return settings["positive_label"]
    return settings["negative_label"]


def determine_true_binary_label(sample, settings):
    """Convert the real species into the lesson's binary label."""
    if sample[settings["label_key"]] == settings["positive_label"]:
        return settings["positive_label"]
    return settings["negative_label"]


def evaluate_prediction(y_pred, y_true):
    """Return True when the prediction matches the real label."""
    return y_pred == y_true


def update_metrics(metrics, y_pred, y_true):
    """Update the metrics dictionary after one prediction."""
    is_correct = evaluate_prediction(y_pred, y_true)

    if is_correct:
        metrics["correct"] += 1
    else:
        metrics["wrong"] += 1

    metrics["total"] += 1
    metrics["y_pred_list"].append(y_pred)


def classify_sample(sample, settings):
    """Keep the classifier step separate from the loop."""
    return determine_binary_label(sample, settings)


def initialize_predictions(dataset, settings, print_each):
    """Run the prediction loop and collect metrics.

    Args:
        dataset (list): The loaded dataset.
        settings (dict): Classifier settings.
        print_each (bool): Whether to print one line per sample.

    Returns:
        dict: Metrics collected during the loop.
    """
    metrics = {
        "correct": 0,
        "wrong": 0,
        "total": 0,
        "y_pred_list": [],
    }

    for sample in dataset:
        y_pred = classify_sample(sample, settings)
        y_true = determine_true_binary_label(sample, settings)
        update_metrics(metrics, y_pred, y_true)

        if print_each:
            print(
                f"id={sample['id']} | true={y_true} | pred={y_pred} | "
                f"petal_length={sample['petal_length']}"
            )

    return metrics


def print_summary(run_label, settings, metrics, accuracy):
    """Print one experiment summary."""
    print(f"\n=== {run_label} ===")
    print("Threshold:", settings["threshold"])
    print("Correct:", metrics["correct"])
    print("Wrong:", metrics["wrong"])
    print("Total:", metrics["total"])
    print("Accuracy (%):", round(accuracy, 2))
    print("All predictions:", metrics["y_pred_list"])


def main():
    """Run the Session 5 experiments."""
    make_print_status("Default run")
    settings, dataset, metrics, accuracy = setup_application()
    print_summary("Default run", settings, metrics, accuracy)

    make_print_status("Positional override run")
    settings, dataset, metrics, accuracy = setup_application(
        "session5/iris_data.csv", 1.8, False, False
    )
    print_summary("Positional override run", settings, metrics, accuracy)

    make_print_status("Keyword override run")
    settings, dataset, metrics, accuracy = setup_application(
        threshold=2.2,
        print_each=False,
    )
    print_summary("Keyword override run", settings, metrics, accuracy)

    make_print_status("Fit-based run")
    settings, dataset, metrics, accuracy = setup_application(
        print_each=False,
        use_fit=True,
    )
    print_summary("Fit-based run", settings, metrics, accuracy)


if __name__ == "__main__":
    main()
