from visitor import MyVisitor
from dist.maciekGPParser import maciekGPParser
from dist.maciekGPLexer import maciekGPLexer
from antlr4 import *


def main():
    lexer = maciekGPLexer(FileStream("examples/factorial.txt"))
    stream = CommonTokenStream(lexer)
    parser = maciekGPParser(stream)
    tree = parser.program()
    visitor = MyVisitor()
    visitor.visit(tree)


if __name__ == '__main__':
    main()
