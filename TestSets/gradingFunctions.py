import math


VERY_BIG_NUMBER = 1000000000
# TODO: replace inf with VERY_BIG_NUMBER and adjust functions to number of outputs


class GradingFunction:
    @staticmethod
    def target_1_1_A(test_case, program_run_context):
        # 1 at any position
        output = program_run_context.get_output()
        if len(output) == 0:
            return math.inf
        squared_diffs = [(out - 1)**2 for out in output]
        return min(squared_diffs)

    @staticmethod
    def target_1_1_B(test_case, program_run_context):
        #789 at any position
        output = program_run_context.get_output()
        if len(output) == 0:
            return math.inf
        squared_diffs = [(out - 789)**2 for out in output]
        return min(squared_diffs)

    @staticmethod
    def target_1_1_C(test_case, program_run_context):
        # 31415 at any position
        output = program_run_context.get_output()
        if len(output) == 0:
            return math.inf
        squared_diffs = [(out - 31415)**2 for out in output]
        return min(squared_diffs)

    @staticmethod
    def target_1_1_D(test_case, program_run_context):
        # 1 at first position
        output = program_run_context.get_output()
        if len(output) == 0:
            return math.inf
        return (output[0] - 1)**2

    @staticmethod
    def target_1_1_E(test_case, program_run_context):
        # 789 at first position
        output = program_run_context.get_output()
        if len(output) == 0:
            return math.inf
        return (output[0] - 789)**2

    @staticmethod
    def target_1_1_F(test_case, program_run_context):
        # 1 as the only output
        output = program_run_context.get_output()
        if len(output) != 1:
            return math.inf
        return (output[0] - 1)**2

    @staticmethod
    def target_1_2_A(test_case, program_run_context):
        # sum of two first inputs of range [0, 9]
        output = program_run_context.get_output()
        if len(output) != 1:
            return math.inf
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_1_2_B(test_case, program_run_context):
        # sum of two first inputs of range [-9, 9]
        output = program_run_context.get_output()
        if len(output) != 1:
            return math.inf
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_1_2_C(test_case, program_run_context):
        # sum of two first inputs of range [-9999, 9999]
        output = program_run_context.get_output()
        if len(output) != 1:
            return math.inf
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_1_2_E(test_case, program_run_context):
        # product of two first inputs of range [-9999, 9999]
        output = program_run_context.get_output()
        if len(output) != 1:
            return math.inf
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_1_3_A(test_case, program_run_context):
        # greater of two first inputs of range [0, 9]
        output = program_run_context.get_output()
        if len(output) != 1:
            return math.inf





