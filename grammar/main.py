from visitor import MyVisitor
from dist.maciekGPParser import maciekGPParser
from dist.maciekGPLexer import maciekGPLexer
from antlr4 import *
from ProgramGenerator.AntlrToProgram import AntlrToProgram
from ProgramGenerator.AntlrToProgram import *


def main():
    lexer = maciekGPLexer(FileStream("examples/fibonacci.txt"))
    stream = CommonTokenStream(lexer)
    parser = maciekGPParser(stream)
    tree = parser.program()
    # visitor = MyVisitor()
    visitor = AntlrToProgram()
    visitor.visit(tree)


if __name__ == '__main__':
    main()
