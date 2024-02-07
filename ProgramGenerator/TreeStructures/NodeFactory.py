from random import random, choice
from .Statements import Assignment, IfStatement, LoopStatement, Print
from .Expressions import Constant, Read, Variable


class NodeFactory:
    @staticmethod
    def get_new_statement(tree_config, program):
        chance = random()
        if chance < tree_config.new_assignment_chance:
            result = Assignment.new_assignment(program)
        elif chance < tree_config.new_if_statement_chance:
            result = IfStatement.new_if_statement(program)
        elif chance < tree_config.new_loop_chance:
            result = LoopStatement.new_loop(program)
        else:
            result = Print.new_print(program)
        return result

    @staticmethod
    def get_new_expression(tree_config, program):
        chance = random()
        if program.variable_counter == 0:
            if choice([True, False]):
                return Constant.new_constant(program)
            return Read.new_read(program)
        if chance < tree_config.new_variable_chance:
            return Variable.random_variable(program)
        elif chance < tree_config.new_constant_chance:
            return Constant.new_constant(program)
        else:
            return Read.new_read(program)
