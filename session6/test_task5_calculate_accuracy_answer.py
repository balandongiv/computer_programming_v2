"""Teacher-only unit tests for Session 6 Task 5.

Open this file in VS Code and use the green play button to run it.
It checks the teacher solution in session6_iris_answer.py.
"""

from pathlib import Path
import sys
import unittest


ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from session6.session6_iris_answer import IrisRuleClassifier
from session6.task5_calculate_accuracy_shared import CalculateAccuracyTestMixin


class TestTask5CalculateAccuracyAnswer(CalculateAccuracyTestMixin, unittest.TestCase):
    """Check the Task 5 accuracy logic in the teacher answer."""

    CLASSIFIER_CLASS = IrisRuleClassifier


if __name__ == "__main__":
    unittest.main()
