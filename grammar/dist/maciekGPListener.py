# Generated from ./maciekGP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .maciekGPParser import maciekGPParser
else:
    from maciekGPParser import maciekGPParser

# This class defines a complete listener for a parse tree produced by maciekGPParser.
class maciekGPListener(ParseTreeListener):

    # Enter a parse tree produced by maciekGPParser#program.
    def enterProgram(self, ctx:maciekGPParser.ProgramContext):
        pass

    # Exit a parse tree produced by maciekGPParser#program.
    def exitProgram(self, ctx:maciekGPParser.ProgramContext):
        pass


    # Enter a parse tree produced by maciekGPParser#statement.
    def enterStatement(self, ctx:maciekGPParser.StatementContext):
        pass

    # Exit a parse tree produced by maciekGPParser#statement.
    def exitStatement(self, ctx:maciekGPParser.StatementContext):
        pass


    # Enter a parse tree produced by maciekGPParser#assignment.
    def enterAssignment(self, ctx:maciekGPParser.AssignmentContext):
        pass

    # Exit a parse tree produced by maciekGPParser#assignment.
    def exitAssignment(self, ctx:maciekGPParser.AssignmentContext):
        pass


    # Enter a parse tree produced by maciekGPParser#ifStatement.
    def enterIfStatement(self, ctx:maciekGPParser.IfStatementContext):
        pass

    # Exit a parse tree produced by maciekGPParser#ifStatement.
    def exitIfStatement(self, ctx:maciekGPParser.IfStatementContext):
        pass


    # Enter a parse tree produced by maciekGPParser#condition.
    def enterCondition(self, ctx:maciekGPParser.ConditionContext):
        pass

    # Exit a parse tree produced by maciekGPParser#condition.
    def exitCondition(self, ctx:maciekGPParser.ConditionContext):
        pass


    # Enter a parse tree produced by maciekGPParser#blockStatement.
    def enterBlockStatement(self, ctx:maciekGPParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by maciekGPParser#blockStatement.
    def exitBlockStatement(self, ctx:maciekGPParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by maciekGPParser#loopStatement.
    def enterLoopStatement(self, ctx:maciekGPParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by maciekGPParser#loopStatement.
    def exitLoopStatement(self, ctx:maciekGPParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by maciekGPParser#print.
    def enterPrint(self, ctx:maciekGPParser.PrintContext):
        pass

    # Exit a parse tree produced by maciekGPParser#print.
    def exitPrint(self, ctx:maciekGPParser.PrintContext):
        pass


    # Enter a parse tree produced by maciekGPParser#expression.
    def enterExpression(self, ctx:maciekGPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by maciekGPParser#expression.
    def exitExpression(self, ctx:maciekGPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by maciekGPParser#nestedExpression.
    def enterNestedExpression(self, ctx:maciekGPParser.NestedExpressionContext):
        pass

    # Exit a parse tree produced by maciekGPParser#nestedExpression.
    def exitNestedExpression(self, ctx:maciekGPParser.NestedExpressionContext):
        pass


    # Enter a parse tree produced by maciekGPParser#read.
    def enterRead(self, ctx:maciekGPParser.ReadContext):
        pass

    # Exit a parse tree produced by maciekGPParser#read.
    def exitRead(self, ctx:maciekGPParser.ReadContext):
        pass


    # Enter a parse tree produced by maciekGPParser#operator.
    def enterOperator(self, ctx:maciekGPParser.OperatorContext):
        pass

    # Exit a parse tree produced by maciekGPParser#operator.
    def exitOperator(self, ctx:maciekGPParser.OperatorContext):
        pass


    # Enter a parse tree produced by maciekGPParser#comparator.
    def enterComparator(self, ctx:maciekGPParser.ComparatorContext):
        pass

    # Exit a parse tree produced by maciekGPParser#comparator.
    def exitComparator(self, ctx:maciekGPParser.ComparatorContext):
        pass


    # Enter a parse tree produced by maciekGPParser#constant.
    def enterConstant(self, ctx:maciekGPParser.ConstantContext):
        pass

    # Exit a parse tree produced by maciekGPParser#constant.
    def exitConstant(self, ctx:maciekGPParser.ConstantContext):
        pass


    # Enter a parse tree produced by maciekGPParser#variable.
    def enterVariable(self, ctx:maciekGPParser.VariableContext):
        pass

    # Exit a parse tree produced by maciekGPParser#variable.
    def exitVariable(self, ctx:maciekGPParser.VariableContext):
        pass



del maciekGPParser