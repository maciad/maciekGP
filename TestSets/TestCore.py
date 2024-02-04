from ProgramGenerator.TreeConfig import TreeConfig


class TestSet:
    def __init__(self):
        self.name = "Name not set"
        self.config = TreeConfig()
        self.test_cases = []
        self.threshold = None
        self.grading_function = None


class TestCase:
    def __init__(self, inp=None, out=None):
        self.input = [] if inp is None else inp
        self.target_output = [] if out is None else out
