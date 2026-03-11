"""Session 4 student template: Refactor Session 3 classifier into reusable functions.

This script demonstrates how to organize sequential logic into modular functions.
We maintain the exact same rule and canonical variable names from Session 3, as later sessions
will import and build upon these specific functions.
"""

import csv


def make_print_status(status_text):
    """Print a status line for user feedback.
    
    Args:
        status_text (str): The text to print.
    """
    print(f"[STATUS] {status_text}")


def determine_binary_label(sample, settings):
    """Return prediction label using threshold rule.
    
    Args:
        sample (dict): A dictionary representing one flower sample.
        settings (dict): The canonical settings dictionary.
        
    Returns:
        str: The predicted species label.
        
    Note: We enforce the use of canonical keys like settings["feature_name"] 
    and settings["threshold"] because later templates depend on these exact names.
    """
    if sample[settings["feature_name"]] < settings["threshold"]:
        return settings["positive_label"]
    else:
        return settings["negative_label"]


def determine_true_binary_label(sample, settings):
    """Convert the sample's true species into a binary label (setosa vs not_setosa).
    
    Args:
        sample (dict): A dictionary representing one flower sample.
        settings (dict): The canonical settings dictionary.
        
    Returns:
        str: The true binary species label.
        
    Note: Later sessions rely on this exact function signature.
    """
    if sample[settings["label_key"]] == settings["positive_label"]:
        return settings["positive_label"]
    else:
        return settings["negative_label"]


def evaluate_prediction(y_pred, y_true):
    """Return True if prediction matches truth, else False."""
    return y_pred == y_true


def classify_sample(sample, settings):
    """Classify one sample using decomposed helper.
    
    Args:
        sample (dict): A single flower dictionary.
        settings (dict): The settings dictionary.
        
    Returns:
        str: The predicted label.
    """
    return determine_binary_label(sample, settings)


def load_iris_data(filepath):
    """Load Iris dataset from a CSV file and return a list of dict samples.
    
    Values read from CSV start as strings, so we convert numeric columns to float.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        list: A list of dictionaries, each representing a sample.
    """
    dataset = []
    with open(filepath, "r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            dataset.append(
                {
                    "id": row["id"],
                    "sepal_length": float(row["sepal_length"]),
                    "sepal_width": float(row["sepal_width"]),
                    "petal_length": float(row["petal_length"]),
                    "petal_width": float(row["petal_width"]),
                    "species": row["species"],
                }
            )
    return dataset


def get_default_settings():
    """Return the Session 2/3 rule settings (kept stable across sessions).
    
    Returns:
        dict: A dictionary of canonical settings.
        
    Note: We enforce these names so the next session's template can import your work without changes.
    """
    return {
        "threshold": 2.0,
        "feature_name": "petal_length",
        "positive_label": "setosa",
        "negative_label": "not_setosa",
        "label_key": "species",
    }


def update_metrics(metrics, y_pred, y_true):
    """Update correct/wrong/total counters and append predictions.
    
    Args:
        metrics (dict): The metrics dictionary tracking accuracy.
        y_pred (str): The predicted label.
        y_true (str): The true label.
        
    Side Effects:
        Modifies the `metrics` dictionary in place.
    """
    is_correct = evaluate_prediction(y_pred, y_true)
    if is_correct:
        metrics["correct"] += 1
    else:
        metrics["wrong"] += 1
    
    # ALWAYS increment metrics["total"] for every sample.
    metrics["total"] += 1
    metrics["y_pred_list"].append(y_pred)


def initialize_predictions(dataset, settings):
    """Run prediction loop and return summary metrics.
    
    Args:
        dataset (list): List of sample dictionaries.
        settings (dict): The canonical settings dictionary.
        
    Returns:
        dict: The final metrics including accuracy.
    """
    metrics = {"correct": 0, "wrong": 0, "total": 0, "y_pred_list": []}

    for sample in dataset:
        y_pred = classify_sample(sample, settings)
        y_true = determine_true_binary_label(sample, settings)
        update_metrics(metrics, y_pred, y_true)
        print(
            f"id={sample['id']} | true={y_true} | pred={y_pred} | "
            f"petal_length={sample['petal_length']}"
        )

    accuracy = (metrics["correct"] / metrics["total"]) * \
        100 if metrics["total"] > 0 else 0.0
    metrics["accuracy"] = accuracy
    return metrics


def setup_application(filepath):
    """Load, configure, and run prediction pipeline."""
    dataset = load_iris_data(filepath)
    settings = get_default_settings()
    result = initialize_predictions(dataset, settings)
    return settings, dataset, result


def main():
    """Entry point for session 4 run."""
    print("=== Student Label ===")
    student_id = "YOUR_ID_HERE"
    full_name = "YOUR_FULL_NAME_HERE"
    print("Student ID:", student_id)
    print("Full Name:", full_name)

    make_print_status("Loading data and running predictions")
    _, _, result = setup_application("session4/iris_data.csv")
    make_print_status("Run complete")

    print("\n=== Final Summary ===")
    print("Correct:", result["correct"])
    print("Wrong:", result["wrong"])
    print("Total:", result["total"])
    print("Accuracy (%):", round(result["accuracy"], 2))
    print("All predictions:", result["y_pred_list"])
    print("\nTry changing the threshold in get_default_settings() to see how accuracy changes!")


# --- Self-Check / Testing Block ---
def _test_update_metrics():
    """Verify that update_metrics correctly increments total for all samples, including wrong ones."""
    test_metrics = {"correct": 0, "wrong": 0, "total": 0, "y_pred_list": []}
    # Provide one correct and one wrong prediction
    update_metrics(test_metrics, "setosa", "setosa")
    update_metrics(test_metrics, "not_setosa", "setosa")
    
    assert test_metrics["total"] == 2, f"Expected total=2, got {test_metrics['total']}. Did you forget to increment total for wrong predictions?"
    print("[Self-Check Passed] update_metrics increments total correctly.")


if __name__ == "__main__":
    _test_update_metrics()
    main()
