# Module Convener Final Answer (session 4)

Reference implementation:

- `session4/session4_iris_model_answer.py`

## Expected Summary Metrics

Using `session4/iris_data.json`, expected output metrics are:

- `Correct: 11`
- `Wrong: 1`
- `Total: 12`
- `Accuracy (%): 91.67`

## Refactor Alignment Check (session 3 -> session 4)

1. session 3 rule if-else is moved into `determine_binary_label(...)`.
2. session 3 truth conversion is moved into `evaluate_prediction(...)`.
3. session 3 per-sample prediction step is wrapped by `classify_sample(...)`.
4. session 3 loop/counters become `initialize_predictions(...)`.
5. session 3 top-level script flow becomes `setup_application(...)` + `main()`.

## Core Grading Checks

1. Uses function decomposition (not sequential-only script).
2. Loads `settings` and `dataset` from JSON.
3. Uses `if __name__ == "__main__":` guard.
4. Keeps classifier rule on `petal_length` + `threshold`.
5. Converts true class to `setosa` vs `not_setosa`.
6. Prints per-sample canonical output line.
7. Reports `correct`, `wrong`, `total`, `accuracy`, and prediction list.
8. Includes student label (ID and full name).

## Suggested Mark Distribution (100)

- Function decomposition and structure: 35
- JSON loading and setup: 20
- Correct prediction/evaluation logic: 30
- Output format and completeness: 15

## Quick Run

```bash
python session4/session4_iris_model_answer.py
```
