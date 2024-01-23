from random import random
from Actions import Assignment, IfStatement, LoopStatement, Print
from Expressions import Constant, Read, Variable


class NodeFactory:
    @staticmethod
    def get_new_action(tree_config, program):
        result = None
        chance = random()
        if chance < tree_config.new_assignment_chance:
            result = Assignment.new_assignment(program)
        elif chance < tree_config.new_if_statement_chance:
            result = IfStatement.new_if_statement(program)
        elif chance < tree_config.new_loop_chance:
            result = LoopStatement.new_loop(program)
        else:                       # new_write_chance is 1
            result = Print.new_print(program)
        return result

    @staticmethod
    def get_new_expression(tree_config, program):
        chance = random()
        if chance < tree_config.new_variable_chance:
            return Variable.random_or_new(program)
        elif chance < tree_config.new_constant_chance:
            return Constant.new_constant(program)
        else:                       # new_read_chance is 1
            return Read.new_read(program)
