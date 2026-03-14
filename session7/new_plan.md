# Recommended Session 7 flow

## 1. Session goal

In Session 7, we continue from Session 6.

In Session 6, students built one class: `IrisRuleClassifier`.

That class had two jobs:

1. **Decide** using one prediction rule
2. **Evaluate** by looping through the dataset and calculating accuracy

Now we want students to see a design problem:

- prediction logic can change from one classifier to another
- evaluation logic often stays the same

So in Session 7, the goal is to teach:

- **inheritance**: child classes reuse code from a parent class
- **polymorphism**: different child objects can be used through the same interface

A simple lesson sentence could be:

> Different classifiers may predict differently, but they can still share the same evaluation behavior.

---

## 2. Start with the design problem

### Teaching explanation

Session 6 worked well for one classifier.

But what happens if we want:

- a `RuleClassifier`
- a `NearestCentroidClassifier`
- a `RandomGuessClassifier`

If every classifier has:

- its own `predict(...)`
- and its own copied `evaluate(...)`

then we create duplication.

### Key points to emphasize

- duplication increases bugs
- fixing one shared behavior becomes harder
- adding a new classifier becomes repetitive work

This creates a natural reason for inheritance.

---

## 3. Introduce the Parent Class (`ClassifierBase`)

Before teaching the first child, students need a parent class to inherit from.

This section is important because it shows what belongs in the base:

### Shared behavior goes into the parent

- `derive_true_label(...)`
- `update_result_counts(...)`
- `calculate_accuracy(...)`
- `evaluate(...)`

### Specific behavior stays in the child

- `predict(...)`
- classifier-specific configuration in `__init__`

---

## Section 1 — Build the parent class: `ClassifierBase`

### Teaching explanation

A parent class is a more general blueprint.

It contains code that many child classes can reuse.

For this lesson:

- every classifier predicts in its own way
- but every classifier can evaluate itself in the same way

So the base class should contain the general evaluation pipeline.

### Good beginner explanation

You can say:

> The base class does not know exactly **how** a classifier predicts.
> But it does know **how to test predictions on a dataset**.

That makes inheritance feel logical.

---

## First task — Define `ClassifierBase`

I recommend the base class scaffold below.

```python
class ClassifierBase:
    def __init__(self):
        self.positive_label = "setosa"
        self.negative_label = "not_setosa"

    def predict(self, sample):
        """Child classes must replace this."""
        raise NotImplementedError("Child class must implement predict()")

    def derive_true_label(self, sample):
        """Convert the dataset species into lesson labels."""
        if sample["species"] == self.positive_label:
            return self.positive_label
        else:
            return self.negative_label

    def update_result_counts(self, correct, wrong, total, y_pred_list, y_pred, y_true):
        """Update counters and prediction list."""
        if y_pred == y_true:
            correct += 1
        else:
            wrong += 1

        total += 1
        y_pred_list.append(y_pred)

        return correct, wrong, total, y_pred_list

    def calculate_accuracy(self, correct, total):
        """Calculate accuracy percentage."""
        if total > 0:
            return (correct / total) * 100
        return 0.0

    def evaluate(self, dataset):
        """Shared evaluation loop for all classifiers."""
        correct = 0
        wrong = 0
        total = 0
        y_pred_list = []

        print("\n=== Start Evaluation ===")

        for sample in dataset:
            y_pred = self.predict(sample)
            y_true = self.derive_true_label(sample)

            correct, wrong, total, y_pred_list = self.update_result_counts(
                correct, wrong, total, y_pred_list, y_pred, y_true
            )

            print(
                f"id={sample['id']} | true={y_true} | pred={y_pred} | "
                f"petal_length={sample['petal_length']}"
            )

        accuracy = self.calculate_accuracy(correct, total)

        return correct, wrong, total, y_pred_list, accuracy
```

---

## Important teaching point in this section

This line is worth explaining carefully:

```python
raise NotImplementedError("Child class must implement predict()")
```

### Beginner-friendly explanation

This means:

> The parent class expects every child class to provide its own `predict()` method.

So the base class is saying:

- “I know evaluation”
- “I do not know your specific prediction rule”

That is a very good transition to inheritance.

---

# Section 2 — The First Child (`RuleClassifier`)

This matches your intended first task.

## Teaching explanation

Now we recreate the Session 6 classifier, but this time it inherits from `ClassifierBase`.

So instead of writing everything again, this child class only needs:

- its own `__init__`
- its own `predict(...)`

It gets the shared methods from the parent.

### First inheritance syntax to teach

```python
class RuleClassifier(ClassifierBase):
```

This means:

> `RuleClassifier` is a child of `ClassifierBase`

---

## First task — The First Child (`RuleClassifier`)

### Suggested explanation before scaffold

A child class can:

- add new attributes
- define its own methods
- reuse methods from the parent

This classifier still uses the Session 6 rule:

- if `petal_length < threshold` → predict `"setosa"`
- otherwise → predict `"not_setosa"`

### Scaffold

```python
class RuleClassifier(ClassifierBase):
    def __init__(self, threshold=2.0):
        # TODO:
        # 1. Call the parent __init__
        # 2. Store threshold in self.threshold
        pass

    def predict(self, sample):
        """Predict using the threshold rule."""
        # TODO:
        # if sample["petal_length"] < self.threshold:
        #     return self.positive_label
        # else:
        #     return self.negative_label
        pass
```

---

## Teach `super()` here

This is the right place to introduce `super()`.

### Beginner explanation

When the child class wants to reuse the parent’s `__init__`, it can call:

```python
super().__init__()
```

That means:

> “Run the parent class initialization first”

So a filled version would look like:

```python
class RuleClassifier(ClassifierBase):
    def __init__(self, threshold=2.0):
        super().__init__()
        self.threshold = threshold
```

That is a very useful beginner milestone.

---

## Checkpoint section

This matches your idea well.

### Checkpoint explanation

After building `RuleClassifier`, show this:

```python
rule_clf = RuleClassifier(threshold=2.0)
results = rule_clf.evaluate(dataset)
```

Then explicitly point out:

> Notice that you can call `rule_clf.evaluate(dataset)` even though you did not write `evaluate()` inside `RuleClassifier`.

That is the practical benefit of inheritance.

### Suggested checkpoint wording

You can say:

> `RuleClassifier` inherits `evaluate()` from `ClassifierBase`.
> So the child class only writes what is different, while reusing what is shared.

---

# Section 3 — The Second Child (`NearestCentroidClassifier`)

This matches your next intended task.

## Teaching explanation

Now students see the real benefit of inheritance.

We can create a completely different classifier without rewriting the evaluation loop.

This new classifier uses a different prediction strategy:

- compare the sample’s `petal_length`
- check which center it is closer to
- return the label of the closer center

So:

- `predict()` changes
- `evaluate()` stays the same

That is the whole point of the design.

---

## Second task — `NearestCentroidClassifier`

### Scaffold

```python
class NearestCentroidClassifier(ClassifierBase):
    def __init__(self, setosa_center=1.5, not_setosa_center=4.5):
        # TODO:
        # 1. Call the parent __init__
        # 2. Store both centers in self
        pass

    def predict(self, sample):
        """Predict by choosing the closer centroid."""
        # TODO:
        # 1. Read petal_length from sample
        # 2. Compute distance to self.setosa_center
        # 3. Compute distance to self.not_setosa_center
        # 4. If closer to setosa center, return self.positive_label
        # 5. Otherwise return self.negative_label
        pass
```

---

## Good explanation for this section

This section is useful because students can now compare two child classes:

- `RuleClassifier.predict(...)`
- `NearestCentroidClassifier.predict(...)`

Both are valid.
Both inherit `evaluate(...)`.

That makes the shared-vs-specific idea very concrete.

---

# Section 4 — Compare both child classes

This section is worth adding, even if you did not mention it explicitly.

It helps students see that inheritance is not just about syntax. It changes the design.

## Teaching explanation

Now we have two classifier objects:

- one uses a threshold rule
- one uses centroid distance

But both can be evaluated in the same way.

This makes the lesson more meaningful before introducing polymorphism.

### Suggested example

```python
rule_clf = RuleClassifier(threshold=2.0)
centroid_clf = NearestCentroidClassifier(setosa_center=1.5, not_setosa_center=4.5)

print("\nRuleClassifier results:")
print(rule_clf.evaluate(dataset))

print("\nNearestCentroidClassifier results:")
print(centroid_clf.evaluate(dataset))
```

This helps students notice:

- different prediction logic
- same shared interface

---

# Section 5 — Introduce polymorphism

Now that students have two child classes, this is the perfect point to teach polymorphism.

## Beginner-friendly explanation

Polymorphism means:

> Different objects can be used in the same way if they share the same method names.

In this lesson:

- `RuleClassifier` has `predict()` and `evaluate()`
- `NearestCentroidClassifier` also has `predict()` and `evaluate()`

So code can work with both, without caring which exact classifier type it receives.

That is the simplest useful definition for beginners.

---

# Section 6 — Suggested polymorphism task

Here is the most suitable task for this session:

## Task: write a function that accepts **any classifier object**

This is better than introducing another class immediately, because it makes the polymorphism idea very visible.

### Why this works well

Students will see that one function can accept:

- `RuleClassifier`
- `NearestCentroidClassifier`
- later, maybe `RandomGuessClassifier`

as long as each object supports the same interface.

---

## Polymorphism task — `run_and_report(classifier, dataset, name)`

### Teaching explanation

This function does not care whether the classifier is:

- a rule classifier
- a centroid classifier
- some future classifier

It only assumes:

- the object has an `evaluate(dataset)` method

That is polymorphism in practice.

### Scaffold

```python
def run_and_report(classifier, dataset, name):
    """Run evaluation for any classifier object."""
    # TODO:
    # 1. Print the classifier name
    # 2. Call classifier.evaluate(dataset)
    # 3. Unpack the returned values
    # 4. Print a short summary
    pass
```

### Example usage

```python
run_and_report(rule_clf, dataset, "RuleClassifier")
run_and_report(centroid_clf, dataset, "NearestCentroidClassifier")
```

### What to emphasize

The function works for both objects because both follow the same interface.

That is the cleanest Session 7 polymorphism task.

---

# Section 7 — Optional extension task for polymorphism

If you want one more small student exercise, this is a good optional extension:

## Optional task: loop over a list of different classifier objects

### Example idea

```python
classifiers = [
    RuleClassifier(threshold=2.0),
    NearestCentroidClassifier(setosa_center=1.5, not_setosa_center=4.5),
]

for clf in classifiers:
    run_and_report(clf, dataset, clf.__class__.__name__)
```

### Why this is useful

It shows that:

- objects can be different types
- but still be handled uniformly

That strongly reinforces polymorphism.

---

# Section 8 — Optional future child (`RandomGuessClassifier`)

You mentioned it as an example, and it makes a nice extension, but I would keep it optional.

## Why optional

For beginners, inheritance + one more child + polymorphism is already enough for one session.

Still, you can mention:

> If we wanted, we could add another classifier later by writing only a new `predict()` method.

That reinforces the design benefit.

### Optional scaffold

```python
import random

class RandomGuessClassifier(ClassifierBase):
    def __init__(self):
        super().__init__()

    def predict(self, sample):
        return random.choice([self.positive_label, self.negative_label])
```

This makes the inheritance idea even more concrete.

---

# Full suggested Session 7 structure

## 1. Session goal

Explain the problem:

- one class in Session 6 was fine
- multiple classifier types create duplication
- inheritance solves the repeated evaluation logic

## 2. Build the parent class: `ClassifierBase`

Teach:

- shared behavior belongs in the base
- `predict()` is left for child classes
- introduce `NotImplementedError`

## 3. First child: `RuleClassifier`

Teach:

- inheritance syntax
- `super().__init__()`
- child writes only the specific rule

## 4. Checkpoint

Show:

- `rule_clf.evaluate(dataset)` works
- even though `evaluate()` was not written in `RuleClassifier`

## 5. Second child: `NearestCentroidClassifier`

Teach:

- a very different prediction strategy
- same inherited evaluation loop

## 6. Compare both child classes

Show:

- different `predict()`
- same `evaluate()`

## 7. Introduce polymorphism

Teach:

- different objects can be used through the same interface

## 8. Polymorphism task

Best task:

- write `run_and_report(classifier, dataset, name)`
- pass different classifier objects into the same function

## 9. Optional extension

Add:

- `RandomGuessClassifier`
- or a list of mixed classifier objects

---

# Full scaffolding template idea for Session 7

```python
class ClassifierBase:
    def __init__(self):
        self.positive_label = "setosa"
        self.negative_label = "not_setosa"

    def predict(self, sample):
        raise NotImplementedError("Child class must implement predict()")

    def derive_true_label(self, sample):
        # TODO:
        # Return self.positive_label or self.negative_label
        pass

    def update_result_counts(self, correct, wrong, total, y_pred_list, y_pred, y_true):
        # TODO:
        # Update counters and return updated values
        pass

    def calculate_accuracy(self, correct, total):
        # TODO:
        # Return accuracy percentage
        pass

    def evaluate(self, dataset):
        # TODO:
        # Shared evaluation loop
        pass


class RuleClassifier(ClassifierBase):
    def __init__(self, threshold=2.0):
        # TODO:
        # Call parent __init__
        # Store threshold
        pass

    def predict(self, sample):
        # TODO:
        # Threshold rule
        pass


class NearestCentroidClassifier(ClassifierBase):
    def __init__(self, setosa_center=1.5, not_setosa_center=4.5):
        # TODO:
        # Call parent __init__
        # Store centers
        pass

    def predict(self, sample):
        # TODO:
        # Compare distance to both centers
        pass


def run_and_report(classifier, dataset, name):
    # TODO:
    # Run classifier.evaluate(dataset)
    # Print summary
    pass
```

---

# Recommended teaching order

I’d teach Session 7 in this order:

1. design problem from Session 6
2. `ClassifierBase`
3. `RuleClassifier`
4. checkpoint on inherited `evaluate()`
5. `NearestCentroidClassifier`
6. comparison between both children
7. polymorphism explanation
8. polymorphism task with `run_and_report(...)`
9. optional extension with another child class
