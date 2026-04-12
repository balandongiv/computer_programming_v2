"""Unit tests for Session 6 Task 4: update_result_counts.

Student check from the project root:
    python3 -m unittest session6.test_task4_update_result_counts
or:
    python3 session6/test_task4_update_result_counts.py

Teacher answer check from the project root:
    python3 session6/test_task4_update_result_counts.py --answer
"""

from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


import unittest

from session6.session6_iris_template import IrisRuleClassifier
from session6.task4_update_result_counts_shared import UpdateResultCountsTestMixin


class TestTask4UpdateResultCounts(UpdateResultCountsTestMixin, unittest.TestCase):
    """Check the Task 4 counter update logic in the student template."""

    CLASSIFIER_CLASS = IrisRuleClassifier


if __name__ == "__main__":
    unittest.main()
