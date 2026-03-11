# Module Convener Final Answer (session 2)

Reference implementation:

- `session2/session2_iris_model_answer.py`

## Core Grading Checks

1. Includes student label (`student_id`, `full_name`).
2. Declares Flower 1 variables with canonical names.
3. Computes and prints `petal_area`.
4. Declares continuity rule variables:
   - `threshold = 2.0`
   - `feature_name = "petal_length"`
   - `positive_label = "setosa"`
   - `negative_label = "not_setosa"`
   - `label_key = "species"`
5. Prints boolean comparison `petal_length < threshold`.
6. Demonstrates `str(...)` and `float(...)` conversions with `type(...)` output.
7. Declares Flower 2 variables with `_2` suffix and prints `petal_area_2`.

## Suggested Mark Distribution (100)

- Correct variable declarations and naming continuity: 35
- Derived values and comparison outputs: 25
- Type conversion and type-check output: 20
- Output format and submission completeness: 20

## Quick Run

```bash
python session2/session2_iris_model_answer.py
```
