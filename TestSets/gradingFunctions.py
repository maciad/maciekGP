VERY_BIG_NUMBER = 1_000_000


class GradingFunction:
    @staticmethod
    def target_1_1_A(test_case, program_run_context):
        # 1 at any position
        output = program_run_context.get_output()
        if len(output) == 0:
            return VERY_BIG_NUMBER
        squared_diffs = [(out - 1)**2 for out in output]
        return min(squared_diffs)

    @staticmethod
    def target_1_1_B(test_case, program_run_context):
        #789 at any position
        output = program_run_context.get_output()
        if len(output) == 0:
            return VERY_BIG_NUMBER
        squared_diffs = [(out - 789)**2 for out in output]
        return min(squared_diffs)

    @staticmethod
    def target_1_1_C(test_case, program_run_context):
        # 31415 at any position
        output = program_run_context.get_output()
        if len(output) == 0:
            return VERY_BIG_NUMBER
        squared_diffs = [(out - 31415)**2 for out in output]
        return min(squared_diffs)

    @staticmethod
    def target_1_1_D(test_case, program_run_context):
        # 1 at first position
        output = program_run_context.get_output()
        if len(output) == 0:
            return VERY_BIG_NUMBER
        return (output[0] - 1)**2

    @staticmethod
    def target_1_1_E(test_case, program_run_context):
        # 789 at first position
        output = program_run_context.get_output()
        if len(output) == 0:
            return VERY_BIG_NUMBER
        return (output[0] - 789)**2

    @staticmethod
    def target_1_1_F(test_case, program_run_context):
        # 1 as the only output
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER * 2
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - 1)**2

    @staticmethod
    def target_1_2_A(test_case, program_run_context):
        # sum of two first inputs of range [0, 9]
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER * 2
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_1_2_B(test_case, program_run_context):
        # sum of two first inputs of range [-9, 9]
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER * 2
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_1_2_C(test_case, program_run_context):
        # sum of two first inputs of range [-9999, 9999]
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER * 2
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_1_2_D(test_case, program_run_context):
        # difference of two first inputs of range [0, 9]
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER * 2
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_1_2_E(test_case, program_run_context):
        # product of two first inputs of range [-9999, 9999]
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER * 2
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_1_3_A(test_case, program_run_context):
        # greater of two first inputs of range [0, 9]
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_1_3_B(test_case, program_run_context):
        # greater of two first inputs of range [-9999, 9999]
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_benchmark_1(test_case, program_run_context):
        # sum on int and float
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_benchmark_17(test_case, program_run_context):
        # sum of squared elements from 1 to n
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER * 2
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - test_case.target_output[0])**2

    @staticmethod
    def target_benchmark_27(test_case, program_run_context):
        # median of 3 inputs
        output = program_run_context.get_output()
        if len(output) == 0:
            penalty = VERY_BIG_NUMBER
            return penalty
        if len(output) > 1:
            penalty = VERY_BIG_NUMBER * len(output)
            return penalty
        return (output[0] - test_case.target_output[0])**2
