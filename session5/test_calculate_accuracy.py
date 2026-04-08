"""Dedicated unit tests for Session 5 Task 1.

This test file checks only the student's calculate_accuracy function.
It does not import the full session5_iris_template module because the rest
of the template may still contain unfinished placeholders.
"""

from __future__ import annotations

import os
import re
import textwrap
import types
import unittest
from pathlib import Path

STUDENT_FILE = Path(
    os.environ.get("SESSION5_IRIS_FILE", "session5/session5_iris_template.py")
)


class StudentCodeError(AssertionError):
    """Raised when the student function cannot be loaded cleanly."""


def load_calculate_accuracy():
    """Extract and return the student's calculate_accuracy function only."""
    source = STUDENT_FILE.read_text(encoding="utf-8")

    match = re.search(
        r"^def calculate_accuracy\(.*?(?=^def |\Z)",
        source,
        flags=re.MULTILINE | re.DOTALL,
    )
    if match is None:
        raise StudentCodeError(
            "Could not find a function named 'calculate_accuracy' in "
            f"{STUDENT_FILE}"
        )

    function_source = textwrap.dedent(match.group(0))
    namespace: dict[str, object] = {}

    try:
        exec(function_source, namespace)
    except SyntaxError as error:
        raise StudentCodeError(
            "Python could not read the calculate_accuracy function yet. "
            "Finish Task 1 first, then run the test again. "
            f"Original error: {error}"
        ) from error

    function = namespace.get("calculate_accuracy")
    if not isinstance(function, types.FunctionType):
        raise StudentCodeError(
            "The name 'calculate_accuracy' was found, but it was not loaded "
            "as a normal Python function."
        )

    return function


class TestCalculateAccuracy(unittest.TestCase):
    """Checks only the behavior required for Task 1."""

    calculate_accuracy = staticmethod(load_calculate_accuracy())

    def test_keyword_arguments_return_expected_percentage(self):
        result = self.calculate_accuracy(correct=8, total=10)
        self.assertEqual(result, 80.0)

    def test_default_arguments_return_zero_without_crashing(self):
        result = self.calculate_accuracy()
        self.assertEqual(result, 0.0)

    def test_zero_total_returns_zero(self):
        result = self.calculate_accuracy(correct=5, total=0)
        self.assertEqual(result, 0.0)

    def test_positional_and_keyword_calls_match(self):
        positional_result = self.calculate_accuracy(3, 4)
        keyword_result = self.calculate_accuracy(total=4, correct=3)
        self.assertEqual(positional_result, keyword_result)
        self.assertEqual(keyword_result, 75.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
