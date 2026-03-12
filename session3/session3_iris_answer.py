"""Session 3: Lists, Loops, and Conditionals for Iris classification.
This script builds on Session 2 by converting variables to dictionaries, assembling a dataset list,
iterating over it, applying a threshold rule, and computing accuracy metrics.
"""

# Session 2 continuity variables (Rule settings). Do not change these.
threshold = 2.0
feature_name = "petal_length"
positive_label = "setosa"
negative_label = "not_setosa"
label_key = "species"

# Task 1: Define dictionaries for flower1 and flower2 using canonical keys
# We remove the sequential variables and group them logically.
flower1 = {
    "id": "flower1",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# TODO: create flower2 dict using values from Session 2 (use same keys as flower1, no _2 suffix)
flower2 = {
    "id": "flower2",
    "sepal_length": 4.9,
    "sepal_width": 3.0,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 2: Build the dataset list
# Combine our dictionaries into a single list
dataset = [flower1, flower2]

# Task 3: Initialize metrics and predictions
correct = 0      # Count of correct predictions
wrong = 0        # Count of wrong predictions
total = 0        # Total samples processed
y_pred_list = [] # List of all predictions made

print("\n=== Start session 3 Prediction Loop ===")

# Task 4 & 5: Iterate and classify
for sample in dataset:
    # 1. Compute prediction (y_pred)
    if sample[feature_name] < threshold:
        y_pred = positive_label
    else:
        y_pred = negative_label
        
    # 2. Derive true label (y_true) from the dataset sample
    if sample[label_key] == positive_label:
        y_true = positive_label
    else:
        y_true = negative_label

    # 3. Update correct or wrong counter
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1

    # 4. ALWAYS increment total for every sample processed
    # Does total increase for each sample? If not, fix it.
    total += 1
    
    # Append the prediction to our list
    y_pred_list.append(y_pred)

    # 5. Print per-sample trace exactly as required
    print(
        f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        f"petal_length={sample['petal_length']}"
    )

# Task 6: Compute and print final metrics
accuracy = (correct / total) * 100 if total > 0 else 0.0

print("\n=== session 3 Summary ===")
print("Correct:", correct)
print("Wrong:", wrong)
print("Total:", total)
print("Accuracy (%):", round(accuracy, 2))
print("All predictions:", y_pred_list)
