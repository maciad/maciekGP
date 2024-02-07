from antlr4 import CommonTokenStream, FileStream

from ProgramGenerator.AntlrToProgram import AntlrToProgram
from ProgramRunContext import ProgramRunContext
from evolution.Evolution import Evolution
from TestSets.TestSetsGenerator import TestSetsGenerator
from grammar.dist.maciekGPLexer import maciekGPLexer
from grammar.dist.maciekGPParser import maciekGPParser


def read_program_from_file(filename):
    lexer = maciekGPLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser = maciekGPParser(stream)
    tree = parser.program()
    program = AntlrToProgram()
    program = program.visit(tree)
    return program

def main():
# READING PROGRAM FROM FILE
    # program = read_program_from_file("grammar/examples/factorial.txt")
    # prc = ProgramRunContext()
    # prc.input = [5]
    # program.invoke(prc)
    # print(prc.get_output())

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

    test_set = TestSetsGenerator.generate_1_1_D()
    best_program = Evolution.perform_evolution(test_set, population_size=1000, max_generations=200, program_size=20)
    # best_program.save_to_file("best_program.txt")
    print(best_program)
    prc = ProgramRunContext()
    prc.input = []
    print(prc.input)
    best_program.invoke(prc)
    print(prc.get_output())


if __name__ == '__main__':
    main()
