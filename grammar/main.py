from ProgramRunContext import ProgramRunContext
from visitor import MyVisitor
from dist.maciekGPParser import maciekGPParser
from dist.maciekGPLexer import maciekGPLexer
from antlr4 import *
from ProgramGenerator.AntlrToProgram import AntlrToProgram
from ProgramGenerator.AntlrToProgram import *


def main():
    lexer = maciekGPLexer(FileStream("examples/benchmark17.txt"))
    stream = CommonTokenStream(lexer)
    parser = maciekGPParser(stream)
    tree = parser.program()
    # visitor = MyVisitor()
    visitor = AntlrToProgram()
    program = visitor.visit(tree)
    prc = ProgramRunContext()
    a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
    prc.input = [a, b, c]
    print(prc.input)
    print(sorted(prc.input)[1])
    program.invoke(prc)
    print(prc.get_output())


if __name__ == '__main__':
    main()
