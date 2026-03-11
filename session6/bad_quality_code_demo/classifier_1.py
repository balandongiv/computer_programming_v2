"""Classifier 1: Detect 'setosa' using a specific rule."""

def predict(sample):
    # Rule 1: Just a silly variation for demonstration
    threshold = 1.0 + (1 * 0.1)
    if sample["petal_length"] < threshold:
        return "setosa"
    return "not_setosa"

# --- COPY-PASTED EVALUATION LOGIC (Start of Duplication) ---
# Imagine this block is 50 lines long.
# If we find a bug here (e.g. wrong accuracy formula), we must fix it in all 10 files!

def evaluate(dataset):
    correct = 0
    total = 0
    for sample in dataset:
        prediction = predict(sample)
        # Truth logic (duplicated!)
        truth = "setosa" if sample["species"] == "setosa" else "not_setosa"
        if prediction == truth:
            correct += 1
        total += 1
    
    # Bug: Division by zero if total is 0 not handled? 
    # Or maybe we want to add F1-score? We'd have to add it 10 times.
    return correct / total if total > 0 else 0.0

# --- (End of Duplication) ---

dataset = [
    {"petal_length": 1.4, "species": "setosa"},
    {"petal_length": 4.5, "species": "versicolor"},
    {"petal_length": 6.0, "species": "virginica"},
]

if __name__ == "__main__":
    print(f"Classifier 1 Accuracy: {evaluate(dataset)}")
