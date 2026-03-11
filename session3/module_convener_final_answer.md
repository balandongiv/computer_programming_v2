# Module Convener Final Answer (session 3)

Reference implementation:

- `session3/session3_iris_model_answer.py`

## Expected Summary Metrics

Using the provided session 3 dataset in the script:

- `Correct: 11`
- `Wrong: 1`
- `Total: 12`
- `Accuracy (%): 91.67`

## Core Grading Checks

1. Uses list + dictionary dataset structure.
2. Uses a `for` loop to process all samples.
3. Uses `if-else` rule with `threshold` and `feature_name`.
4. Converts true class using `label_key`, `positive_label`, `negative_label`.
5. Updates `correct`, `wrong`, `total`, and `y_pred_list`.
6. Prints per-sample line in canonical format.
7. Prints final metrics and predictions list.
8. Includes student label (ID and full name).
9. Uses no function definitions in session 3 solution.

## Suggested Mark Distribution (100)

- Correct list/loop/conditional classifier implementation: 45
- Correct truth conversion and metric counting: 25
- Output format continuity with session 4 bridge: 15
- Student label and overall completeness: 15

## Quick Run

```bash
python session3/session3_iris_model_answer.py
```
