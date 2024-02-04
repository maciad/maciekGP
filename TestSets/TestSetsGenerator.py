from TestSets.TestCore import TestSet, TestCase
from TestSets.gradingFunctions import GradingFunction
import random


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

    @staticmethod
    def generate_1_1_B():
        ts = TestSet()
        ts.name = "1_1_B"
        ts.threshold = 789 * 0.02
        ts.grading_function = GradingFunction.target_1_1_B
        ts.test_cases = [
            TestCase([], [789])
        ]
        return ts

    @staticmethod
    def generate_1_1_C():
        ts = TestSet()
        ts.name = "1_1_C"
        ts.threshold = 31415 * 0.02
        ts.grading_function = GradingFunction.target_1_1_C
        ts.test_cases = [
            TestCase([], [31415]),
            TestCase([1], [31415]),
            TestCase([2, 12], [31415]),
        ]
        return ts

    @staticmethod
    def generate_1_1_D():
        ts = TestSet()
        ts.name = "1_1_D"
        ts.threshold = 0.0
        ts.grading_function = GradingFunction.target_1_1_D
        ts.test_cases = [
            TestCase([], [1]),
            TestCase([1], [1]),
            TestCase([2, 5], [1]),
            TestCase([123], [1]),
        ]
        return ts

    @staticmethod
    def generate_1_1_E():
        ts = TestSet()
        ts.name = "1_1_E"
        ts.threshold = 789 * 0.02
        ts.grading_function = GradingFunction.target_1_1_E
        ts.test_cases = [
            TestCase([], [789]),
            TestCase([1], [789]),
            TestCase([2, 5], [789]),
            TestCase([123], [789]),
        ]
        return ts

    @staticmethod
    def generate_1_1_F():
        ts = TestSet()
        ts.name = "1_1_F"
        ts.threshold = 0.0
        ts.grading_function = GradingFunction.target_1_1_F
        ts.test_cases = [
            TestCase([], [1]),
            TestCase([1], [1]),
            TestCase([2, 5], [1]),
            TestCase([123], [1]),
        ]
        return ts

    @staticmethod
    def generate_1_2_A():
        ts = TestSet()
        ts.name = "1_2_A"
        ts.threshold = 0.0
        ts.grading_function = GradingFunction.target_1_2_A
        for i in range(10):
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            tc = TestCase([a, b], [a + b])
            ts.test_cases.append(tc)
        return ts

    @staticmethod
    def generate_1_2_B():
        ts = TestSet()
        ts.name = "1_2_B"
        ts.threshold = 0.0
        ts.grading_function = GradingFunction.target_1_2_B
        for i in range(10):
            a = random.randint(-9, 9)
            b = random.randint(-9, 9)
            tc = TestCase([a, b], [a + b])
            ts.test_cases.append(tc)
        return ts

    @staticmethod
    def generate_1_2_C():
        ts = TestSet()
        ts.name = "1_2_C"
        ts.threshold = 0.0
        ts.grading_function = GradingFunction.target_1_2_C
        for i in range(10):
            a = random.randint(-9999, 9999)
            b = random.randint(-9999, 9999)
            tc = TestCase([a, b], [a + b])
            ts.test_cases.append(tc)
        return ts

    @staticmethod
    def generate_1_2_D():
        ts = TestSet()
        ts.name = "1_2_D"
        ts.threshold = 0.0
        ts.grading_function = GradingFunction.target_1_2_D
        for i in range(10):
            a = random.randint(-9999, 9999)
            b = random.randint(-9999, 9999)
            tc = TestCase([a, b], [a - b])
            ts.test_cases.append(tc)
        return ts

    @staticmethod
    def generate_1_2_E():
        ts = TestSet()
        ts.name = "1_2_E"
        ts.threshold = 0.0
        ts.grading_function = GradingFunction.target_1_2_E
        for i in range(10):
            a = random.randint(-9999, 9999)
            b = random.randint(-9999, 9999)
            tc = TestCase([a, b], [a * b])
            ts.test_cases.append(tc)
        return ts

    @staticmethod
    def generate_1_3_A():
        ts = TestSet()
        ts.name = "1_3_A"
        ts.threshold = 0.0
        ts.grading_function = GradingFunction.target_1_3_A
        for i in range(10):
            a = random.randint(0, 99)
            b = random.randint(0, 99)
            tc = TestCase([a, b], [max(a, b)])
            ts.test_cases.append(tc)
        return ts
