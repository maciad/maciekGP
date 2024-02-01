from antlr4 import *
from grammar.dist.maciekGPLexer import maciekGPLexer
from ProgramGenerator.AntlrToProgram import *
from ProgramGenerator.TreeGenerator import *
from ProgramGenerator.TreeConfig import TreeConfig
from ProgramRunContext import ProgramRunContext


def main():
    prc = ProgramRunContext()
    prc.input = [7, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    prc.max_executed_actions = 1000

    # lexer = maciekGPLexer(FileStream("grammar/examples/max_number.txt"))
    # stream = CommonTokenStream(lexer)
    # parser = maciekGPParser(stream)
    # tree = parser.program()
    # program = AntlrToProgram()
    # tree_xd = program.visit(tree)
    # tree_xd.invoke(prc)
    # print('output', prc.get_output())

    config = TreeConfig(max_depth=5)
    # program_2 = generate_program_from_config(config, depth_percentage=100)
    program_2 = generate_program_node_count(min_node_count=15)
    # program_2.full_grow()
    print(program_2)

    type_to_mutate = program_2.config.type_to_mutate()
    if program_2.has_node_of_type(type_to_mutate):
        print('mutating', type_to_mutate)
        program_2.mutate(type_to_mutate)
        print(program_2)

    program_2.save_to_file('program_2.txt')

    # execute program_2 using lexer and parser
    # program_2.invoke(prc)
    # print(prc.output)

    # p = generate_program_node_count(12)


if __name__ == '__main__':
    main()
