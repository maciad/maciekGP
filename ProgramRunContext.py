import random
from enum import Enum


class ProgramRunContext:

    class Strategy(Enum):
        INPUT_OR_ZERO = 0
        LOCK_LAST_INPUT = 1
        LOOP_INPUT = 2

    def __init__(self):
        self.input = []
        self.input_copy = []
        self.output = []
        self.variables = {}
        self.elapsed_milliseconds = -1
        self.elapsed_ticks = -1
        self.random = random.Random()
        self.actions = 0
        self.executed_actions = 0
        self.max_executed_actions = -1

    strategy = Strategy.INPUT_OR_ZERO

    def has_timed_out(self):
        return self.max_executed_actions == self.executed_actions

    def increment_execution_time(self):
        self.executed_actions += 1
        if self.executed_actions > self.max_executed_actions:
            raise Exception("OutOfTimeException")

    def pop(self):
        result = 0
        if self.strategy == self.Strategy.INPUT_OR_ZERO:
            if len(self.input) > 0:
                result = self.input[0]
                self.input = self.input[1:]
                return result
            return 0
        elif self.strategy == self.Strategy.LOCK_LAST_INPUT:
            if len(self.input) > 1:
                result = self.input[0]
                self.input = self.input[1:]
                return result
            elif self.input:
                return self.input[0]
            return 0
        elif self.strategy == self.Strategy.LOOP_INPUT:
            if not self.input:
                return 0
            if not self.input_copy:
                self.input_copy = self.input.copy()
            result = self.input_copy[0]
            self.input_copy = self.input_copy[1:]
            return result
        return result      # should never happen

    def push(self, value):
        self.output.append(int(value))

    def __str__(self):
        result = "Input: " + ", ".join(map(str, self.input)) + "\nOutput: " + ", ".join(map(str, self.output)) + "\nVariables: " + ", ".join(
            [f"{key} = {value}" for key, value in self.variables.items()]
        )
        return result

    def to_string_tabbed(self, tab=1):
        result = ""
        t = "\t" * tab
        for line in self.__str__().split("\n"):
            result += t + line + "\n"
        return result

    def get_output(self):
        return self.output
