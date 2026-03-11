def fit_threshold_from_setosa(dataset, fallback_threshold=2.0):
    """Learn a simple threshold as mean petal_length over setosa samples."""
    total = 0.0
    count = 0

    for sample in dataset:
        if sample["species"] == "setosa":
            total += sample["petal_length"]
            count += 1

    return total / count if count > 0 else fallback_threshold
