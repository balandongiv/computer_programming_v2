# Module Convener Final Answer (session 5)

Reference implementation:

- `session5/session5_iris_model_answer.py`

## Expected Metrics

For `session5/iris_data.json`:

- Default run (`threshold=2.0`):
  - `Correct: 11`
  - `Wrong: 1`
  - `Total: 12`
  - `Accuracy (%): 91.67`
- Positional override run (`threshold=1.8`):
  - `Correct: 12`
  - `Wrong: 0`
  - `Total: 12`
  - `Accuracy (%): 100.0`
- Keyword override run (`threshold=2.2`):
  - `Correct: 11`
  - `Wrong: 1`
  - `Total: 12`
  - `Accuracy (%): 91.67`

## Core Grading Checks

1. Keeps session 4 function names and classifier behavior.
2. Adds positional-argument extension in function signatures.
3. Adds keyword arguments with defaults (`None`/`True`) and fallback logic.
4. Demonstrates one positional override call and one keyword override call.
5. Uses JSON loading and maintains canonical labels/features.
6. Reports summary metrics for all three runs.
7. Includes student label and `if __name__ == "__main__":` guard.

## Suggested Mark Distribution (100)

- Correct positional/keyword function design: 40
- Correct fallback/default logic and classifier consistency: 30
- Correct run outputs for default/positional/keyword calls: 20
- Output format and submission completeness: 10

## Quick Run

```bash
python session5/session5_iris_model_answer.py
```
