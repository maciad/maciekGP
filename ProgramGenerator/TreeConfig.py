import random
from ProgramGenerator.TreeStructures.Expressions import Variable, Constant, NestedExpression
from ProgramGenerator.TreeStructures.Operator import Operator
from ProgramGenerator.TreeStructures.Statements import Assignment, IfStatement, Print, BlockStatement
from ProgramGenerator.TreeStructures.Program import Program
from ProgramGenerator.TreeStructures.Comparator import Condition, Comparator


class TreeConfig:
    def __init__(self, max_execution_time=1000, min_node_count=15, max_depth=6):
        # # Tree Basic Data
        self.max_execution_time = max_execution_time
        self.min_node_count = min_node_count
        self.max_depth = max_depth

        # Tree Variables range
        self.min_variable_value = 0
        self.max_variable_value = 25

        # Tree Structure Generation Data
        self.new_assignment_chance_factor = 10
        self.new_if_statement_chance_factor = 5
        self.new_loop_chance_factor = 5
        self.new_print_chance_factor = 5

        self.new_variable_chance_factor = 20
        self.new_constant_chance_factor = 20
        self.new_read_chance_factor = 3

        self.grow_program_chance_factor = 5
        self.grow_if_statement_chance_factor = 2
        self.grow_print_chance_factor = 2
        self.grow_assignment_chance_factor = 2
        self.grow_nested_expression_chance_factor = 2
        self.grow_condition_chance_factor = 2
        self.grow_block_statement_chance_factor = 5

        # Tree Evolution Data
        self.mutation_chance = 0.3
        self.mutate_program_factor = 0.5
        self.mutate_variable_factor = 0.5
        self.mutate_constant_factor = 0.5
        self.mutate_comparator_factor = 0.5
        self.mutate_operator_factor = 0.5
        self.mutate_block_statement_factor = 0.1

        self.mutation_remove_chance_factor = 0.5
        self.mutation_swap_chance_factor = 0.5

        self.crossover_loop_factor = 25
        self.crossover_if_factor = 25
        self.crossover_print_factor = 0
        self.crossover_assignment_factor = 25
        self.crossover_variable_factor = 0
        self.crossover_constant_factor = 0
        self.crossover_nested_expression_factor = 25
        self.crossover_comparator_factor = 0
        self.crossover_operator_factor = 0
        self.crossover_block_statement_factor = 0

        # Precalculated Values
        self.new_assignment_chance = 0
        self.new_if_statement_chance = 0
        self.new_loop_chance = 0
        self.new_print_chance = 0

        self.new_variable_chance = 0
        self.new_constant_chance = 0
        self.new_read_chance = 0

        self.grow_program_chance = 0
        self.grow_if_statement_chance = 0
        self.grow_print_chance = 0
        self.grow_assignment_chance = 0
        self.grow_nested_expression_chance = 0
        self.grow_condition_chance = 0
        self.grow_block_statement_chance = 0

        self.mutate_program_chance = 0
        self.mutate_variable_chance = 0
        self.mutate_constant_chance = 0
        self.mutate_comparator_chance = 0
        self.mutate_operator_chance = 0
        self.mutate_block_statement_chance = 0

        self.mutation_remove_chance = 0

        self.crossover_loop_chance = 0
        self.crossover_if_chance = 0
        self.crossover_print_chance = 0
        self.crossover_assignment_chance = 0
        self.crossover_variable_chance = 0
        self.crossover_constant_chance = 0
        self.crossover_nested_expression_chance = 0
        self.crossover_comparator_chance = 0
        self.crossover_operator_chance = 0
        self.crossover_block_statement_chance = 0

        # Initialize random seed
        self.r = random.Random()

        # Precalculate values
        self.precalculate_grow()
        self.precalculate_mutation()
        self.precalculate_crossover()

    def precalculate_grow(self):
        self.precalculate_grow_statements()
        self.precalculate_grow_expressions()
        self.precalculate_grow_program()

    def precalculate_grow_statements(self):
        total_chance = (
            self.new_assignment_chance_factor +
            self.new_if_statement_chance_factor +
            self.new_loop_chance_factor +
            self.new_print_chance_factor
        )
        self.new_assignment_chance = self.new_assignment_chance_factor / total_chance
        self.new_if_statement_chance = self.new_if_statement_chance_factor / total_chance + self.new_assignment_chance
        self.new_loop_chance = self.new_loop_chance_factor / total_chance + self.new_if_statement_chance
        self.new_print_chance = self.new_print_chance_factor / total_chance + self.new_loop_chance

    def precalculate_grow_expressions(self):
        total_chance = (
            self.new_variable_chance_factor +
            self.new_constant_chance_factor +
            self.new_read_chance_factor
        )
        self.new_variable_chance = self.new_variable_chance_factor / total_chance
        self.new_constant_chance = self.new_constant_chance_factor / total_chance + self.new_variable_chance
        self.new_read_chance = self.new_read_chance_factor / total_chance + self.new_constant_chance

    def precalculate_grow_program(self):
        # Sum all chances
        sum_chances = (
            self.grow_program_chance_factor +
            self.grow_if_statement_chance_factor +
            self.grow_print_chance_factor +
            self.grow_assignment_chance_factor +
            self.grow_nested_expression_chance_factor +
            self.grow_condition_chance_factor +
            self.grow_block_statement_chance_factor
        )

        # Calculate chances and offset them
        self.grow_program_chance = self.grow_program_chance_factor / sum_chances
        self.grow_if_statement_chance = (self.grow_if_statement_chance_factor / sum_chances) + self.grow_program_chance
        self.grow_print_chance = (self.grow_print_chance_factor / sum_chances) + self.grow_if_statement_chance
        self.grow_assignment_chance = (self.grow_assignment_chance_factor / sum_chances) + self.grow_print_chance
        self.grow_nested_expression_chance = (self.grow_nested_expression_chance_factor / sum_chances) + self.grow_assignment_chance
        self.grow_condition_chance = (self.grow_condition_chance_factor / sum_chances) + self.grow_nested_expression_chance
        self.grow_block_statement_chance = (self.grow_block_statement_chance_factor / sum_chances) + self.grow_condition_chance

    def precalculate_mutation(self):
        # Sum all chances
        sum_chances = (
            self.mutate_program_factor +
            self.mutate_variable_factor +
            self.mutate_constant_factor +
            self.mutate_comparator_factor +
            self.mutate_operator_factor +
            self.mutate_block_statement_factor
        )

        # Calculate chances and offset them
        self.mutate_program_chance = self.mutate_program_factor / sum_chances
        self.mutate_variable_chance = (self.mutate_variable_factor / sum_chances) + self.mutate_program_chance
        self.mutate_constant_chance = (self.mutate_constant_factor / sum_chances) + self.mutate_variable_chance
        self.mutate_comparator_chance = (self.mutate_comparator_factor / sum_chances) + self.mutate_constant_chance
        self.mutate_operator_chance = (self.mutate_operator_factor / sum_chances) + self.mutate_comparator_chance
        self.mutate_block_statement_chance = (self.mutate_block_statement_factor / sum_chances) + self.mutate_operator_chance

        self.mutation_remove_chance = self.mutation_remove_chance_factor / (self.mutation_remove_chance_factor + self.mutation_swap_chance_factor)

    def precalculate_crossover(self):
        # Sum all chances
        sum_chances = (
            self.crossover_loop_factor +
            self.crossover_if_factor +
            self.crossover_print_factor +
            self.crossover_assignment_factor +
            self.crossover_variable_factor +
            self.crossover_constant_factor +
            self.crossover_nested_expression_factor +
            self.crossover_comparator_factor +
            self.crossover_operator_factor +
            self.crossover_block_statement_factor
        )

        # Calculate chances and offset them
        self.crossover_loop_chance = self.crossover_loop_factor / sum_chances
        self.crossover_if_chance = (self.crossover_if_factor / sum_chances) + self.crossover_loop_chance
        self.crossover_print_chance = (self.crossover_print_factor / sum_chances) + self.crossover_if_chance
        self.crossover_assignment_chance = (self.crossover_assignment_factor / sum_chances) + self.crossover_print_chance
        self.crossover_variable_chance = (self.crossover_variable_factor / sum_chances) + self.crossover_assignment_chance
        self.crossover_constant_chance = (self.crossover_constant_factor / sum_chances) + self.crossover_variable_chance
        self.crossover_nested_expression_chance = (self.crossover_nested_expression_factor / sum_chances) + self.crossover_constant_chance
        self.crossover_comparator_chance = (self.crossover_comparator_factor / sum_chances) + self.crossover_nested_expression_chance
        self.crossover_operator_chance = (self.crossover_operator_factor / sum_chances) + self.crossover_comparator_chance
        self.crossover_block_statement_chance = (self.crossover_block_statement_factor / sum_chances) + self.crossover_operator_chance

    def type_to_grow(self):
        chance = self.r.random()
        if chance < self.grow_program_chance:
            return Program
        elif chance < self.grow_if_statement_chance:
            return IfStatement
        elif chance < self.grow_print_chance:
            return Print
        elif chance < self.grow_assignment_chance:
            return Assignment
        elif chance < self.grow_nested_expression_chance:
            return NestedExpression
        elif chance < self.grow_condition_chance:
            return Condition
        elif chance < self.grow_block_statement_chance:
            return BlockStatement
        raise Exception('Invalid type')

    def type_to_mutate(self):
        chance = self.r.random()
        if chance < self.mutate_program_chance:
            return Program
        elif chance < self.mutate_variable_chance:
            return Variable
        elif chance < self.mutate_constant_chance:
            return Constant
        elif chance < self.mutate_comparator_chance:
            return Comparator
        elif chance < self.mutate_operator_chance:
            return Operator
        return BlockStatement
