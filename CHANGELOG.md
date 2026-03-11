# Changelog

## Unreleased

### Changed
- Refactored devcontainer setup to move create/start commands into scripts for easier debugging.
- Added Yarn APT repository key setup to the devcontainer create script.

## Session 2
- Renamed and unified student templates into `session2_iris_template.py` as the canonical file.
- Fixed code formatting in `ses2.tex` (removed LaTeX escapes from underscores, fixed smart quotes).
- Added a "Hands-on file" callout box and checkpoints with common mistakes in `ses2.tex`.
- Updated `session2_iris_template.py` to match variables exactly, add clear comments, and remove in-line solutions.
- Corrected typos (e.g., `sepal_lenght` -> `sepal_length`).
- Added a Summary & Review section at the end of Session 2.

## Session 3
- Renamed student template to `session3_iris_template.py`.
- Fixed malformed dictionary code example in `ses3.tex` and removed out-of-context "robots" metaphor.
- Added a "Python Lists in One Minute" primer to `ses3.tex` instead of telling students to read about it on their own.
- Modified `session3_iris_template.py` to remove sequential variables, create `flower1` and `flower2` dictionaries, loop over `dataset`, and appropriately calculate metrics ensuring `total` increments for every sample.
- Added checkpoints and common mistakes callouts in `ses3.tex`.
- Concluded Session 3 with a Summary \& Review section containing reflection questions and a micro-exercise.

## Session 4
- Renamed student template to `session4_iris_template.py` and deleted redundant files.
- Refactored `session4_iris_template.py` to add clear docstrings, self-check test block for `total` metric logic, and structured logic for refactoring code into functions.
- Updated `ses4.tex` with clear "Goal" and "You will work in" callouts, a functions primer, and explanations for canonical keys.
- Removed formatting artifacts from `ses4.tex`.
- Concluded Session 4 with a Summary \& Review section containing reflection questions and a real-world hook.

## Session 5
- Renamed student template to `session5_iris_template.py` and deleted redundant files.
- Refactored `session5_iris_template.py` to extend Session 4 functions with optional positional and keyword arguments, plus a `use_fit` option using imported helper module `fit_threshold_from_setosa`.
- Clarified `ses5.tex` with explicit running context to avoid `ModuleNotFoundError` and structured instructions using callouts for positional vs keyword parameters.
- Addressed code formatting and added `print_summary` to avoid code duplication in printing runs.
- Concluded Session 5 with a Summary \& Review section containing common mistake explanations, reflection questions, and a micro-exercise.

## Session 6
- Renamed student template to `session6_iris_template.py` and deleted redundant files.
- Refactored `session6_iris_template.py` to use an Object-Oriented approach with `IrisRuleClassifier` containing `__init__`, `predict`, and `evaluate` methods, ensuring total logic count bug is fixed.
- Updated `ses6.tex` to include "Goal" and "You will work in" callouts, and removed embedded solutions, moving to a Checkpoint/Common Mistake structure.
- Clarified the meaning of `self` and importance of canonical attribute names in `ses6.tex`.
- Concluded Session 6 with a Summary \& Review section containing reflection questions and a micro-exercise.

## Session 7
- Renamed student template to `session7_iris_template.py` and deleted redundant files.
- Refactored `session7_iris_template.py` to implement a `ClassifierBase` class, from which `RuleClassifier` and `NearestCentroidClassifier` inherit. Added a `RandomGuessClassifier` optional exercise.
- Demonstrated polymorphism by evaluating a list of different classifier objects within a loop.
- Updated `ses7.tex` with definitions for "Sample" and "Dataset", and used "You will work in", "Checkpoint", and "Troubleshooting" callouts to better structure the session.
- Emphasized fixing the evaluation logic bug (making sure `total` increments for all samples unconditionally).

## Session 8
- Renamed student template to `session8_iris_template.py` and modularized functions into `iris_session8_utils.py` and `iris_session8_models.py`.
- Added Numpy capabilities (e.g., masking, centroid finding) properly typed and documented in python files.
- Updated `ses8.tex` with "You will work in", explicit definitions for `X` and `y`, axis 0 vs axis 1 explanations, checkpoints, and troubleshooting advice.
- Concluded Session 8 with a Summary and Reflection Section.

## Session 9
- Renamed student template to `session9_iris_template.py` and modularized evaluation scripts into `iris_eval.py` and `session9_plot_accuracy.py`.
- Refactored Python code to use systematic parameter sweeping and generated box/line plots.
- Updated `ses9.tex` with a Checkpoint structure, detailed instructions for experiments and dataframe processing, and a summary section.
