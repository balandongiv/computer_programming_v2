Here’s a clean Session 6 teaching template you can reuse.

Your Session 5 file already has the functional pieces we want to refactor into a class: `make_print_status`, `compute_threshold_prediction`, `derive_true_label`, `update_result_counts`, `calculate_accuracy`, `run_prediction_loop`, and `print_summary`. That makes it a good bridge from “functions” to “class with state + behavior.”

## Recommended Session 6 flow

### 1. Session goal

In Session 6, we refactor our Session 5 functional pipeline into a class called `IrisRuleClassifier`.

The purpose of this class is to keep:

- **configuration** together, such as the threshold and lesson labels
- **behavior** together, such as prediction and evaluation methods

This helps students see that a class is just a way to group related data and related actions in one place.

---

## Section 1 — Define the blueprint and data (`__init__`)

### Teaching explanation

A class is like a **blueprint**.

When we write:

```python
classifier = IrisRuleClassifier()
```

Python creates one object from that blueprint.

Inside the class, `self` means:

> “this specific object”

So if we write:

```python
self.threshold = threshold
```

we are storing the threshold **inside this classifier object**.

That means later methods can use:

```python
self.threshold
self.positive_label
self.negative_label
```

without needing those values passed again and again.

### Starter code to explain

```python
class IrisRuleClassifier:
    def __init__(self, threshold=2.0):
        # Store configuration inside the instance (self)
        self.threshold = threshold

        # We enforce these attribute names so later sessions can reuse your class!
        self.positive_label = "setosa"
        self.negative_label = "not_setosa"
```

### What students should understand here

- `__init__` runs when the object is created
- `self.threshold` stores data in the object
- the object now “remembers” its own configuration

---

## Section 2 — Introduce methods using `make_print_status`

This is a very good first method because it is simple and not cognitively heavy.

### Bridge from function to method

Before:

```python
def make_print_status(status_text):
    print(f"[STATUS] {status_text}")
```

As a class method:

```python
def print_status(self, status_text):
    print(f"[STATUS] {status_text}")
```

### Teaching explanation

A **method** is just a function that lives inside a class.

The main difference is:

- a normal function stands alone
- a method belongs to an object, so it receives `self`

Even if this method does not use `self.threshold` yet, we still include `self` because it belongs to the class.

### Example usage

```python
classifier = IrisRuleClassifier()
classifier.print_status("Build dataset")
```

This reads nicely:

> “Ask this classifier object to print a status.”

---

## Section 3 — Student task: write `compute_threshold_prediction`

This is the best next task because students now see a real benefit of storing data in `self`.

### Teaching explanation

In Session 5, the function used global names like:

- `THRESHOLD`
- `POSITIVE_LABEL`
- `NEGATIVE_LABEL`

In Session 6, we want students to replace those with object attributes:

- `self.threshold`
- `self.positive_label`
- `self.negative_label`

That is the key idea of the refactor.

### What students should do

They should complete this method so that:

- if `petal_length < self.threshold`, return `self.positive_label`
- otherwise, return `self.negative_label`

### Scaffold

```python
def compute_threshold_prediction(self, sample):
    """Predict the label for one flower sample.

    Args:
        sample (dict): One flower sample.

    Returns:
        str: The predicted label.
    """
    # TODO:
    # 1. Check sample["petal_length"]
    # 2. Compare it with self.threshold
    # 3. Return self.positive_label or self.negative_label

    pass
```

### Teacher note

This is the moment to explicitly say:

> In a class, we usually stop depending on global variables.
> Instead, we read values from `self`.

---

## Section 4 — Student task: write `derive_true_label`

This is another good beginner task because it mirrors the earlier function and keeps the logic simple.

### Teaching explanation

We still want only two lesson labels:

- `"setosa"`
- `"not_setosa"`

So this method converts the real species into the simplified lesson label.

### Important beginner note

I would **not** make `derive_true_label` return `correct, wrong, total, y_pred_list`.

That would be confusing, because `derive_true_label` has only one job:

> derive the true label for one sample

So it should return only:

```python
y_true
```

The method that should manage `correct`, `wrong`, `total`, and `y_pred_list` is `update_result_counts` or the prediction loop.

### Scaffold

```python
def derive_true_label(self, sample):
    """Convert the real species into the lesson label.

    Args:
        sample (dict): One flower sample.

    Returns:
        str: The true label for this lesson.
    """
    # TODO:
    # If sample["species"] is the positive class,
    # return self.positive_label
    # Otherwise return self.negative_label

    pass
```

---

## Section 5 — Student task: write `update_result_counts`

This is one of the missing pieces you should include, because it is part of evaluation behavior.

### Teaching explanation

This method updates:

- `correct`
- `wrong`
- `total`
- `y_pred_list`

We keep the return values explicit because beginners usually understand visible data flow better than hidden mutation.

So instead of introducing more advanced patterns, we let the method return all updated values.

### Scaffold

```python
def update_result_counts(self, correct, wrong, total, y_pred_list, y_pred, y_true):
    """Update the counters and prediction list for one sample.

    Returns:
        tuple: Updated correct, wrong, total, y_pred_list
    """
    # TODO:
    # 1. Compare y_pred and y_true
    # 2. Update correct or wrong
    # 3. Increase total
    # 4. Append y_pred to y_pred_list
    # 5. Return all updated values

    pass
```

### Why this section matters

This is where students see:

- one method can help another method
- classes are not only for prediction, but also for evaluation behavior

---

## Section 6 — Student task: write `calculate_accuracy`

This is another missing section worth adding because it completes the evaluation pipeline.

### Teaching explanation

Accuracy is:

```python
(correct / total) * 100
```

But we also protect beginners from division-by-zero errors.

### Scaffold

```python
def calculate_accuracy(self, correct, total):
    """Calculate accuracy percentage."""
    # TODO:
    # If total is greater than 0, compute accuracy
    # Otherwise return 0.0

    pass
```

---

## Section 7 — Student task: write `run_prediction_loop`

This is the big “put everything together” class method.

### Teaching explanation

This method is valuable because it shows how methods collaborate:

1. compute prediction
2. derive true label
3. update counts
4. return final results

That is the strongest example of “behavior bundled in a class.”

### Scaffold

```python
def run_prediction_loop(self, dataset):
    """Run prediction and evaluation on the dataset.

    Returns:
        tuple: correct, wrong, total, y_pred_list
    """
    # TODO:
    # 1. Start correct, wrong, total at 0
    # 2. Start y_pred_list as an empty list
    # 3. Loop through each sample in dataset
    # 4. Call self.compute_threshold_prediction(sample)
    # 5. Call self.derive_true_label(sample)
    # 6. Call self.update_result_counts(...)
    # 7. Print one line for each sample
    # 8. Return correct, wrong, total, y_pred_list

    pass
```

### Teacher note

This is a good place to reinforce method calls like:

```python
self.compute_threshold_prediction(sample)
self.derive_true_label(sample)
```

That helps students see that methods inside the same class can call each other through `self`.

---

## Section 8 — Student task: write `print_summary`

This should also be included, because it keeps the output behavior with the classifier.

### Scaffold

```python
def print_summary(self, correct, wrong, total, y_pred_list, accuracy):
    """Print the final results."""
    # TODO:
    # Print the summary values in a beginner-friendly format

    pass
```

---

## Section 9 — Keep dataset setup outside the class

I recommend **not** moving `setup_application_list()` into the class yet.

### Why

Because the Session 6 objective is:

- bundle **classifier configuration**
- bundle **prediction/evaluation behavior**

The dataset builder is separate from the classifier itself.

That keeps the class focused and avoids overloading beginners with too many ideas at once.

---

## Full scaffolding template for students

```python
class IrisRuleClassifier:
    def __init__(self, threshold=2.0):
        # Store configuration inside the instance (self)
        self.threshold = threshold

        # We enforce these attribute names so later sessions can reuse your class!
        self.positive_label = "setosa"
        self.negative_label = "not_setosa"

    def print_status(self, status_text):
        """Print a small status message."""
        print(f"[STATUS] {status_text}")

    def compute_threshold_prediction(self, sample):
        """Predict the label for one flower sample.

        Args:
            sample (dict): One flower sample.

        Returns:
            str: The predicted label.
        """
        # TODO:
        # if sample["petal_length"] < self.threshold:
        #     return self.positive_label
        # else:
        #     return self.negative_label
        pass

    def derive_true_label(self, sample):
        """Convert the real species into the lesson label.

        Args:
            sample (dict): One flower sample.

        Returns:
            str: The true label for this lesson.
        """
        # TODO:
        # if sample["species"] == self.positive_label:
        #     return self.positive_label
        # else:
        #     return self.negative_label
        pass

    def update_result_counts(self, correct, wrong, total, y_pred_list, y_pred, y_true):
        """Update counters and prediction list.

        Returns:
            tuple: Updated correct, wrong, total, y_pred_list
        """
        # TODO:
        # Compare y_pred and y_true
        # Update correct or wrong
        # Increase total
        # Append y_pred to y_pred_list
        # Return updated values
        pass

    def calculate_accuracy(self, correct, total):
        """Calculate accuracy percentage."""
        # TODO:
        # if total > 0:
        #     accuracy = (correct / total) * 100
        # else:
        #     accuracy = 0.0
        # return accuracy
        pass

    def run_prediction_loop(self, dataset):
        """Run prediction and evaluation on the dataset.

        Returns:
            tuple: correct, wrong, total, y_pred_list
        """
        # TODO:
        # correct = 0
        # wrong = 0
        # total = 0
        # y_pred_list = []

        # print("\n=== Start Session 6 Prediction Loop ===")

        # for sample in dataset:
        #     y_pred = self.compute_threshold_prediction(sample)
        #     y_true = self.derive_true_label(sample)
        #     correct, wrong, total, y_pred_list = self.update_result_counts(
        #         correct, wrong, total, y_pred_list, y_pred, y_true
        #     )
        #
        #     print(
        #         f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        #         f"petal_length={sample['petal_length']}"
        #     )

        # return correct, wrong, total, y_pred_list
        pass

    def print_summary(self, correct, wrong, total, y_pred_list, accuracy):
        """Print the final results."""
        # TODO:
        # print("\n=== Session 6 Summary ===")
        # print("Correct:", correct)
        # print("Wrong:", wrong)
        # print("Total:", total)
        # print("Accuracy (%):", round(accuracy, 2))
        # print("All predictions:", y_pred_list)
        pass
```

---

## Suggested `main()` for Session 6

```python
def main():
    dataset = setup_application_list()

    classifier = IrisRuleClassifier(threshold=2.0)

    classifier.print_status("Build dataset")
    classifier.print_status("Run prediction loop")

    correct, wrong, total, y_pred_list = classifier.run_prediction_loop(dataset)
    accuracy = classifier.calculate_accuracy(correct, total)

    classifier.print_status("Print summary")
    classifier.print_summary(correct, wrong, total, y_pred_list, accuracy)
```

---

## Best teaching order

I’d teach it in this order:

1. `__init__`
2. `print_status`
3. `compute_threshold_prediction`
4. `derive_true_label`
5. `update_result_counts`
6. `calculate_accuracy`
7. `run_prediction_loop`
8. `print_summary`
9. `main`

That order moves from:

- simplest method
- to logic method
- to evaluation method
- to orchestration method
