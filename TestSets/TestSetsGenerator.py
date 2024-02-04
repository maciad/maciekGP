from TestSets.TestCore import TestSet, TestCase
from TestSets.gradingFunctions import GradingFunction


class TestSetsGenerator:
    @staticmethod
    def save_test_set(filename, test_set):
        pass

    @staticmethod
    def generate_1_1_A():
        ts = TestSet()
        ts.name = "1_1_A"
        ts.threshold = 0.0
        ts.grading_function = GradingFunction.target_1_1_A
        ts.test_cases = [
            TestCase([], [1]),
            TestCase([1], [1]),
            TestCase([2], [1]),
            TestCase([123], [1]),
        ]
        return ts
