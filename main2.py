from antlr4 import *
from grammar.dist.maciekGPLexer import maciekGPLexer
from ProgramGenerator.AntlrToProgram import *
from ProgramGenerator.TreeGenerator import *
from ProgramGenerator.TreeConfig import TreeConfig
from ProgramRunContext import ProgramRunContext
from evolution.Evolution import Evolution
from TestSets.TestSetsGenerator import TestSetsGenerator
from Crossover import Crossover


def main():
    prc = ProgramRunContext()
    prc.input = [7, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    prc.max_executed_actions = 1000

# READING PROGRAM FROM FILE
    # lexer = maciekGPLexer(FileStream("grammar/examples/max_number.txt"))
    # stream = CommonTokenStream(lexer)
    # parser = maciekGPParser(stream)
    # tree = parser.program()
    # program = AntlrToProgram()
    # tree_xd = program.visit(tree)
    # tree_xd.invoke(prc)
    # print('output', prc.get_output())

# GENERATING PROGRAM
    # program = generate_program_node_count(12)
    # print(program)

# MUTATION
    # program = generate_program_node_count(15)
    # print(program)
    # if program.can_be_mutated():
    #     type_to_mutate = program.config.type_to_mutate()
    #     while not program.has_node_of_type(type_to_mutate):
    #         type_to_mutate = program.config.type_to_mutate()
    #     print('mutating', type_to_mutate)
    #     program.mutate(type_to_mutate)
    #     print(program)

# CROSSOVER
    # p1 = generate_program_node_count(10)
    # p2 = generate_program_node_count(10)
    # print(p1)
    # print(p2)
    # p3, p4 = Crossover.cross_programs(p1, p2, TreeConfig())
    # print(p3)
    # print(p4)

    test_set = TestSetsGenerator.generate_1_1_A()
    Evolution.perform_evolution(test_set)



if __name__ == '__main__':
    main()
