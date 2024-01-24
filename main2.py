from antlr4 import *
from grammar.dist.maciekGPLexer import maciekGPLexer
from ProgramGenerator.AntlrToProgram import *


def main():
    lexer = maciekGPLexer(FileStream("grammar/examples/fibonacci.txt"))
    stream = CommonTokenStream(lexer)
    parser = maciekGPParser(stream)
    tree = parser.program()
    visitor = AntlrToProgram()
    visitor.visit(tree)


if __name__ == '__main__':
    main()
