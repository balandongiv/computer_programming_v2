"""Unit tests for Session 6 Task 5: calculate_accuracy.

Student check from the project root:
    python3 -m unittest session6.test_task5_calculate_accuracy
or:
    python3 session6/test_task5_calculate_accuracy.py
"""

from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


import unittest

from session6.session6_iris_template import IrisRuleClassifier
from session6.task5_calculate_accuracy_shared import CalculateAccuracyTestMixin


class TestTask5CalculateAccuracy(CalculateAccuracyTestMixin, unittest.TestCase):
    """Check the Task 5 accuracy logic in the student template."""

    CLASSIFIER_CLASS = IrisRuleClassifier


if __name__ == "__main__":
    unittest.main()
