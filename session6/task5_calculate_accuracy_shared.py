"""Shared Task 5 test cases for Session 6.

Both the student test file and the teacher-answer test file import this module
so the assertions stay identical.
"""


class CalculateAccuracyTestMixin:
    """Shared assertions for Task 5."""

    CLASSIFIER_CLASS = None

    def setUp(self):
        if self.CLASSIFIER_CLASS is None:
            raise ValueError("CLASSIFIER_CLASS must be set on the test class.")
        self.classifier = self.CLASSIFIER_CLASS(threshold=2.0)

    def test_returns_full_accuracy_for_all_correct(self):
        accuracy = self.classifier.calculate_accuracy(correct=50, total=50)
        self.assertEqual(accuracy, 100.0)

    def test_returns_partial_accuracy_percentage(self):
        accuracy = self.classifier.calculate_accuracy(correct=40, total=50)
        self.assertEqual(accuracy, 80.0)

    def test_returns_zero_for_empty_dataset(self):
        accuracy = self.classifier.calculate_accuracy(correct=0, total=0)
        self.assertEqual(accuracy, 0.0)
