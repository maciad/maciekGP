from ProgramGenerator.TreeConfig import TreeConfig
from ProgramGenerator.TreeStructures.Statements import *
from ProgramGenerator.TreeStructures.Expressions import *
from ProgramGenerator.TreeStructures.Comparator import *

from copy import deepcopy
import random


class Crossover:
    @staticmethod
    def get_type_to_cross(tree_config):
        chance = random.random()
        if chance < tree_config.crossover_loop_chance:
            return LoopStatement
        elif chance < tree_config.crossover_if_chance:
            return IfStatement
        elif chance < tree_config.crossover_print_chance:
            return Print
        elif chance < tree_config.crossover_assignment_chance:
            return Assignment
        elif chance < tree_config.crossover_variable_chance:
            return Variable
        elif chance < tree_config.crossover_constant_chance:
            return Constant
        elif chance < tree_config.crossover_nested_expression_chance:
            return NestedExpression
        elif chance < tree_config.crossover_comparator_chance:
            return Comparator
        elif chance < tree_config.crossover_operator_chance:
            return Operator
        else:
            return BlockStatement

    @staticmethod
    def cross_programs(program1, program2, tree_config):
        p1_copy = deepcopy(program1)
        p2_copy = deepcopy(program2)

        p1_nodes = p1_copy.get_nodes()
        p2_nodes = p2_copy.get_nodes()

        # remove root nodes
        p1_nodes = p1_nodes[1:]
        p2_nodes = p2_nodes[1:]

        type_to_cross = Crossover.get_type_to_cross(tree_config)

        p1_matching_nodes = [node for node in p1_nodes if isinstance(node, type_to_cross)]
        p2_matching_nodes = [node for node in p2_nodes if isinstance(node, type_to_cross)]

        for _ in range(40):
            if len(p1_matching_nodes) > 0 and len(p2_matching_nodes) > 0:
                break
            type_to_cross = Crossover.get_type_to_cross(tree_config)
            p1_matching_nodes = [node for node in p1_nodes if isinstance(node, type_to_cross)]
            p2_matching_nodes = [node for node in p2_nodes if isinstance(node, type_to_cross)]

        if len(p1_matching_nodes) == 0 or len(p2_matching_nodes) == 0:
            print('failed to cross nodes')
            return None, None

        p1_node = random.choice(p1_matching_nodes)
        p1_node_depth = p1_node.get_depth()
        p2_node = Crossover.get_p2_node_by_probability(p2_matching_nodes, p1_node_depth)
        if p2_node:
            Node.cross_nodes(p1_node, p2_node)
            print('crossed nodes', type_to_cross)
            return p1_copy, p2_copy
        raise Exception('failed to cross nodes')

    @staticmethod
    def get_p2_node_by_probability(p2_matching_nodes, p1_node_depth):
        nodes_depths = {node: node.get_depth() for node in p2_matching_nodes}
        nodes_depths = {k: v for k, v in nodes_depths.items() if v <= 1 + (2 * p1_node_depth)}

        subtrees_count_lower = sum(1 for v in nodes_depths.values() if v < p1_node_depth)
        subtrees_count_equal = sum(1 for v in nodes_depths.values() if v == p1_node_depth)
        subtrees_count_greater = sum(1 for v in nodes_depths.values() if v > p1_node_depth)

        if subtrees_count_lower == 0 or subtrees_count_greater == 0:
            if subtrees_count_equal == 0:
                return random.choice(p2_matching_nodes)
            equal_nodes = [k for k, v in nodes_depths.items() if v == p1_node_depth]
            return random.choice(equal_nodes)

        avg_size_lower = sum(v for v in nodes_depths.values() if v < p1_node_depth) / subtrees_count_lower
        avg_size_greater = sum(v for v in nodes_depths.values() if v > p1_node_depth) / subtrees_count_greater

        factor_eq = 1.0 / p1_node_depth
        factor_lt = (1 - p1_node_depth) / (1 + avg_size_lower / avg_size_greater)

        if subtrees_count_equal == 0:
            factor_eq = 0

        chance = random.random()
        if chance < factor_eq or subtrees_count_equal > 0:
            return random.choice([k for k, v in nodes_depths.items() if v == p1_node_depth])
        elif chance < factor_eq + factor_lt:
            return random.choice([k for k, v in nodes_depths.items() if v < p1_node_depth])
        return random.choice([k for k, v in nodes_depths.items() if v > p1_node_depth])

    @staticmethod
    def get_p2_node_random(p2_matching_nodes , p1_node_depth):
        pass

























