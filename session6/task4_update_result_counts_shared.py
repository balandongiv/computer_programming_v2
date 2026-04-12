"""Shared Task 4 test cases for Session 6.

Both the student test file and the teacher-answer test file import this module
so the assertions stay identical.
"""


class UpdateResultCountsTestMixin:
    """Shared assertions for Task 4."""

    CLASSIFIER_CLASS = None

    def setUp(self):
        if self.CLASSIFIER_CLASS is None:
            raise ValueError("CLASSIFIER_CLASS must be set on the test class.")
        self.classifier = self.CLASSIFIER_CLASS(threshold=2.0)

    def test_updates_counts_for_correct_prediction(self):
        correct, wrong, total, y_pred_list = self.classifier.update_result_counts(
            correct=0,
            wrong=0,
            total=0,
            y_pred_list=[],
            y_pred="setosa",
            y_true="setosa",
        )

        self.assertEqual(correct, 1)
        self.assertEqual(wrong, 0)
        self.assertEqual(total, 1)
        self.assertEqual(y_pred_list, ["setosa"])

    def test_updates_counts_for_wrong_prediction(self):
        correct, wrong, total, y_pred_list = self.classifier.update_result_counts(
            correct=2,
            wrong=1,
            total=3,
            y_pred_list=["setosa", "not_setosa", "setosa"],
            y_pred="not_setosa",
            y_true="setosa",
        )

        self.assertEqual(correct, 2)
        self.assertEqual(wrong, 2)
        self.assertEqual(total, 4)
        self.assertEqual(
            y_pred_list,
            ["setosa", "not_setosa", "setosa", "not_setosa"],
        )
