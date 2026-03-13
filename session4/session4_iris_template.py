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


def compute_prediction(sample, threshold):
    """Convert the sample's true species into a binary label (setosa vs not_setosa).
    
    Args:
        sample (dict): A dictionary representing one flower sample.
        settings (dict): The canonical settings dictionary.
        
    Returns:
        str: The true binary species label.
        
    Note: Later sessions rely on this exact function signature.
    """

    positive_label = "setosa"
    negative_label = "not_setosa"
    feature_name = "petal_length"
    if sample[feature_name] < threshold:
        y_pred = positive_label
    else:
        y_pred = negative_label
    return y_pred

def derive_true_label(sample, settings):
    label_key = "species"
    positive_label = "setosa"
    negative_label = "not_setosa"
    # 2. Derive true label (y_true) from the dataset sample
    if sample[label_key] == positive_label:
        y_true = positive_label
    else:
        y_true = negative_label
    return y_true


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
        y_pred = compute_prediction(sample, settings)
        y_true = derive_true_label(sample, settings)
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

def setup_application_list():
    """Combination of  Task 1 and Task 2 in session 3, but now in a function."""
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


    # make_print_status("Loading data and running predictions")
    _, _, result = setup_application("session4/iris_data.csv")


if __name__ == "__main__":
    main()
