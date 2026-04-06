"""Session 3: Lists, Loops, and Conditionals for Iris classification.
This script builds on Session 2 by converting variables to dictionaries, assembling a dataset list,
iterating over it, applying a threshold rule, and computing accuracy metrics.
"""

# Session 2 continuity variables (Rule settings). Do not change these."""
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"
LABEL_KEY = "species"

# Initialize metrics and predictions
correct = 0      # Count of correct predictions
wrong = 0        # Count of wrong predictions
total = 0        # Total samples processed
y_pred_list = []  # List of all predictions made


# We remove the sequential variables and group them logically.
flower1 = {
    "id": "flower1",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 1: Create A dictionary for second flower
flower2 = {
    "id": "flower2",
    "sepal_length": 4.9,
    "sepal_width": 3.0,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 2: Create list of dictionaries
# Combine our dictionaries into a single list
dataset = [flower1, flower2]

print("\n=== Start session 3 Prediction Loop ===")

# Task 3: Create a for loop to process the dataset
for sample in dataset:
    print(sample["id"], sample["petal_length"], sample["species"])

    # Task 4: Use an if-else statement to classify each sample based on the threshold rule
    GG = sample[FEATURE_NAME]
    if sample[FEATURE_NAME] < THRESHOLD:
        y_pred = POSITIVE_LABEL
    else:
        y_pred = NEGATIVE_LABEL

    # Task 5:. Derive true label (y_true) from the dataset sample
    if sample[LABEL_KEY] == POSITIVE_LABEL:
        y_true = POSITIVE_LABEL
    else:
        y_true = NEGATIVE_LABEL

    # Task 6: Update correct or wrong counter
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1

    # Task 7: ALWAYS increment total for every sample processed
    total += 1

    # Task 8: Append the prediction to our list
    y_pred_list.append(y_pred)

    # Task 9: Print per-sample trace exactly as required
    print(
        f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        f"petal_length={sample['petal_length']}"
    )

# Task 10: Compute and print final metrics
accuracy = (correct / total) * 100 if total > 0 else 0.0

print("\n=== session 3 Summary ===")
print("Correct:", correct)
print("Wrong:", wrong)
print("Total:", total)
print("Accuracy (%):", round(accuracy, 2))
print("All predictions:", y_pred_list)
