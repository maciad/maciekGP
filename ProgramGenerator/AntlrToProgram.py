from grammar.dist.maciekGPParser import maciekGPParser
from grammar.dist.maciekGPVisitor import maciekGPVisitor
from .TreeStructures.Program import *
from .TreeStructures.Statements import *
from .TreeStructures.Operator import *
from .TreeStructures.Comparator import *
from .TreeStructures.Expressions import *


class AntlrToProgram(maciekGPVisitor):
    def visitProgram(self, ctx: maciekGPParser.ProgramContext):
        children = [self.visit(child) for child in ctx.children]
        return Program(seed=None, children=children)

    def visitStatement(self, ctx: maciekGPParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitBlockStatement(self, ctx: maciekGPParser.BlockStatementContext):
        return BlockStatement([self.visit(child) for child in ctx.children[1:-1]])

    # def visitLoopStatement(self, ctx: maciekGPParser.LoopStatementContext):
    #     if ctx.constant():
    #         print(ctx.constant().getText())
    #         repeat_times = self.visit(ctx.constant())
    #     else:
    #         print(ctx.variable().getText())
    #         # print()
    #         repeat_times = self.visit(ctx.variable())
    #     return LoopStatement(repeat_times, self.visit(ctx.blockStatement()))

    def visitLoopStatement(self, ctx: maciekGPParser.LoopStatementContext):
        if ctx.constant():
            return LoopStatement(self.visit(ctx.constant()), self.visit(ctx.blockStatement()))
        return LoopStatement(self.visit(ctx.variable()), self.visit(ctx.blockStatement()))

    def visitRead(self, ctx: maciekGPParser.ReadContext):
        # print(ctx.getText())
        # return Read().evaluate(ctx)
        return Read()

    def visitPrint(self, ctx: maciekGPParser.PrintContext):
        # print(ctx.getChild(2).getText())
        return Print(self.visit(ctx.expression()))

    def visitIfStatement(self, ctx: maciekGPParser.IfStatementContext):
        # if ctx.else_():
        #     return IfStatement(self.visit(ctx.condition()), self.visit(ctx.blockStatement(0)),
        #                        self.visit(ctx.blockStatement(1)))
        # return IfStatement(self.visit(ctx.condition()), self.visit(ctx.blockStatement(0)))
        if ctx.children[6].getText() == "else":
            return IfStatement(self.visit(ctx.condition()), self.visit(ctx.blockStatement(0)), self.visit(ctx.blockStatement(1)))
        return IfStatement(self.visit(ctx.condition()), self.visit(ctx.blockStatement(0)))

    def visitCondition(self, ctx: maciekGPParser.ConditionContext):
        return Condition(self.visit(ctx.expression(0)), self.visit(ctx.comparator()), self.visit(ctx.expression(1)))

    def visitAssignment(self, ctx: maciekGPParser.AssignmentContext):
        return Assignment(self.visit(ctx.variable()), self.visit(ctx.expression()))

    def visitExpression(self, ctx: maciekGPParser.ExpressionContext):
        return self.visit(ctx.getChild(0))

    def visitNestedExpression(self, ctx: maciekGPParser.NestedExpressionContext):
        print(ctx.getText())
        return NestedExpression(self.visit(ctx.expression(0)), self.visit(ctx.operator()), self.visit(ctx.expression(1)))

    def visitConstant(self, ctx: maciekGPParser.ConstantContext):
        # print(ctx.getText())
        return Constant(int(ctx.getChild(0).getText()))

    def visitVariable(self, ctx: maciekGPParser.VariableContext):
        # print(ctx.getText())
        return Variable(int(ctx.getText()[2:]))

    def visitOperator(self, ctx: maciekGPParser.OperatorContext):
        print(ctx.getChild(0).getText())
        return Operator(ctx.getChild(0).getText())

    def visitComparator(self, ctx: maciekGPParser.ComparatorContext):
        return Comparator(ctx.getChild(0).getText())
