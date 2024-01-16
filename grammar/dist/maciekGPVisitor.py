# Generated from ./maciekGP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .maciekGPParser import maciekGPParser
else:
    from maciekGPParser import maciekGPParser

# This class defines a complete generic visitor for a parse tree produced by maciekGPParser.

class maciekGPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by maciekGPParser#program.
    def visitProgram(self, ctx:maciekGPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#statement.
    def visitStatement(self, ctx:maciekGPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#assignment.
    def visitAssignment(self, ctx:maciekGPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#ifStatement.
    def visitIfStatement(self, ctx:maciekGPParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#condition.
    def visitCondition(self, ctx:maciekGPParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#blockStatement.
    def visitBlockStatement(self, ctx:maciekGPParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#loopStatement.
    def visitLoopStatement(self, ctx:maciekGPParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#print.
    def visitPrint(self, ctx:maciekGPParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#expression.
    def visitExpression(self, ctx:maciekGPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#nestedExpression.
    def visitNestedExpression(self, ctx:maciekGPParser.NestedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#read.
    def visitRead(self, ctx:maciekGPParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#operator.
    def visitOperator(self, ctx:maciekGPParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#comparator.
    def visitComparator(self, ctx:maciekGPParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#else.
    def visitElse(self, ctx:maciekGPParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#constant.
    def visitConstant(self, ctx:maciekGPParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by maciekGPParser#variable.
    def visitVariable(self, ctx:maciekGPParser.VariableContext):
        return self.visitChildren(ctx)



del maciekGPParser