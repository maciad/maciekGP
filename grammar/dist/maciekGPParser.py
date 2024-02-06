# Generated from ./maciekGP.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,42,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,55,8,3,
        1,4,1,4,1,4,1,4,1,5,1,5,5,5,63,8,5,10,5,12,5,66,9,5,1,5,1,5,1,6,
        1,6,1,6,3,6,73,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,
        8,86,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,
        13,1,13,1,14,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,0,2,1,0,11,15,1,0,16,21,99,0,31,1,0,0,0,2,41,1,0,0,0,4,
        43,1,0,0,0,6,47,1,0,0,0,8,56,1,0,0,0,10,60,1,0,0,0,12,69,1,0,0,0,
        14,76,1,0,0,0,16,85,1,0,0,0,18,87,1,0,0,0,20,93,1,0,0,0,22,95,1,
        0,0,0,24,97,1,0,0,0,26,99,1,0,0,0,28,101,1,0,0,0,30,32,3,2,1,0,31,
        30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,35,1,0,0,
        0,35,36,5,0,0,1,36,1,1,0,0,0,37,42,3,4,2,0,38,42,3,6,3,0,39,42,3,
        12,6,0,40,42,3,14,7,0,41,37,1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,
        41,40,1,0,0,0,42,3,1,0,0,0,43,44,3,28,14,0,44,45,5,1,0,0,45,46,3,
        16,8,0,46,5,1,0,0,0,47,48,5,2,0,0,48,49,5,3,0,0,49,50,3,8,4,0,50,
        51,5,4,0,0,51,54,3,10,5,0,52,53,5,5,0,0,53,55,3,10,5,0,54,52,1,0,
        0,0,54,55,1,0,0,0,55,7,1,0,0,0,56,57,3,16,8,0,57,58,3,24,12,0,58,
        59,3,16,8,0,59,9,1,0,0,0,60,64,5,6,0,0,61,63,3,2,1,0,62,61,1,0,0,
        0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,64,
        1,0,0,0,67,68,5,7,0,0,68,11,1,0,0,0,69,72,5,8,0,0,70,73,3,26,13,
        0,71,73,3,28,14,0,72,70,1,0,0,0,72,71,1,0,0,0,73,74,1,0,0,0,74,75,
        3,10,5,0,75,13,1,0,0,0,76,77,5,9,0,0,77,78,5,3,0,0,78,79,3,16,8,
        0,79,80,5,4,0,0,80,15,1,0,0,0,81,86,3,26,13,0,82,86,3,28,14,0,83,
        86,3,18,9,0,84,86,3,20,10,0,85,81,1,0,0,0,85,82,1,0,0,0,85,83,1,
        0,0,0,85,84,1,0,0,0,86,17,1,0,0,0,87,88,5,3,0,0,88,89,3,16,8,0,89,
        90,3,22,11,0,90,91,3,16,8,0,91,92,5,4,0,0,92,19,1,0,0,0,93,94,5,
        10,0,0,94,21,1,0,0,0,95,96,7,0,0,0,96,23,1,0,0,0,97,98,7,1,0,0,98,
        25,1,0,0,0,99,100,5,25,0,0,100,27,1,0,0,0,101,102,5,22,0,0,102,103,
        5,25,0,0,103,29,1,0,0,0,6,33,41,54,64,72,85
    ]

class maciekGPParser ( Parser ):

    grammarFileName = "maciekGP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'if'", "'('", "')'", "'else'", 
                     "'{'", "'}'", "'loop'", "'print'", "'read()'", "'*'", 
                     "'/'", "'+'", "'-'", "'%'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'x_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "WS", "INT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_ifStatement = 3
    RULE_condition = 4
    RULE_blockStatement = 5
    RULE_loopStatement = 6
    RULE_print = 7
    RULE_expression = 8
    RULE_nestedExpression = 9
    RULE_read = 10
    RULE_operator = 11
    RULE_comparator = 12
    RULE_constant = 13
    RULE_variable = 14

    ruleNames =  [ "program", "statement", "assignment", "ifStatement", 
                   "condition", "blockStatement", "loopStatement", "print", 
                   "expression", "nestedExpression", "read", "operator", 
                   "comparator", "constant", "variable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    COMMENT=23
    WS=24
    INT=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(maciekGPParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(maciekGPParser.StatementContext)
            else:
                return self.getTypedRuleContext(maciekGPParser.StatementContext,i)


        def getRuleIndex(self):
            return maciekGPParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = maciekGPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4195076) != 0)):
                    break

            self.state = 35
            self.match(maciekGPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(maciekGPParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(maciekGPParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(maciekGPParser.LoopStatementContext,0)


        def print_(self):
            return self.getTypedRuleContext(maciekGPParser.PrintContext,0)


        def getRuleIndex(self):
            return maciekGPParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = maciekGPParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.assignment()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.ifStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.loopStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.print_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(maciekGPParser.VariableContext,0)


        def expression(self):
            return self.getTypedRuleContext(maciekGPParser.ExpressionContext,0)


        def getRuleIndex(self):
            return maciekGPParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = maciekGPParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.variable()
            self.state = 44
            self.match(maciekGPParser.T__0)
            self.state = 45
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(maciekGPParser.ConditionContext,0)


        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(maciekGPParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(maciekGPParser.BlockStatementContext,i)


        def getRuleIndex(self):
            return maciekGPParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = maciekGPParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(maciekGPParser.T__1)
            self.state = 48
            self.match(maciekGPParser.T__2)
            self.state = 49
            self.condition()
            self.state = 50
            self.match(maciekGPParser.T__3)
            self.state = 51
            self.blockStatement()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 52
                self.match(maciekGPParser.T__4)
                self.state = 53
                self.blockStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(maciekGPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(maciekGPParser.ExpressionContext,i)


        def comparator(self):
            return self.getTypedRuleContext(maciekGPParser.ComparatorContext,0)


        def getRuleIndex(self):
            return maciekGPParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = maciekGPParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.expression()
            self.state = 57
            self.comparator()
            self.state = 58
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(maciekGPParser.StatementContext)
            else:
                return self.getTypedRuleContext(maciekGPParser.StatementContext,i)


        def getRuleIndex(self):
            return maciekGPParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = maciekGPParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(maciekGPParser.T__5)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4195076) != 0):
                self.state = 61
                self.statement()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(maciekGPParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self):
            return self.getTypedRuleContext(maciekGPParser.BlockStatementContext,0)


        def constant(self):
            return self.getTypedRuleContext(maciekGPParser.ConstantContext,0)


        def variable(self):
            return self.getTypedRuleContext(maciekGPParser.VariableContext,0)


        def getRuleIndex(self):
            return maciekGPParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = maciekGPParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(maciekGPParser.T__7)
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 70
                self.constant()
                pass
            elif token in [22]:
                self.state = 71
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 74
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(maciekGPParser.ExpressionContext,0)


        def getRuleIndex(self):
            return maciekGPParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = maciekGPParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(maciekGPParser.T__8)
            self.state = 77
            self.match(maciekGPParser.T__2)
            self.state = 78
            self.expression()
            self.state = 79
            self.match(maciekGPParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(maciekGPParser.ConstantContext,0)


        def variable(self):
            return self.getTypedRuleContext(maciekGPParser.VariableContext,0)


        def nestedExpression(self):
            return self.getTypedRuleContext(maciekGPParser.NestedExpressionContext,0)


        def read(self):
            return self.getTypedRuleContext(maciekGPParser.ReadContext,0)


        def getRuleIndex(self):
            return maciekGPParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = maciekGPParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.constant()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.variable()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.nestedExpression()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.read()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NestedExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(maciekGPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(maciekGPParser.ExpressionContext,i)


        def operator(self):
            return self.getTypedRuleContext(maciekGPParser.OperatorContext,0)


        def getRuleIndex(self):
            return maciekGPParser.RULE_nestedExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestedExpression" ):
                listener.enterNestedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestedExpression" ):
                listener.exitNestedExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestedExpression" ):
                return visitor.visitNestedExpression(self)
            else:
                return visitor.visitChildren(self)




    def nestedExpression(self):

        localctx = maciekGPParser.NestedExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_nestedExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(maciekGPParser.T__2)
            self.state = 88
            self.expression()
            self.state = 89
            self.operator()
            self.state = 90
            self.expression()
            self.state = 91
            self.match(maciekGPParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return maciekGPParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = maciekGPParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(maciekGPParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return maciekGPParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = maciekGPParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return maciekGPParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = maciekGPParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(maciekGPParser.INT, 0)

        def getRuleIndex(self):
            return maciekGPParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = maciekGPParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(maciekGPParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(maciekGPParser.INT, 0)

        def getRuleIndex(self):
            return maciekGPParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = maciekGPParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(maciekGPParser.T__21)
            self.state = 102
            self.match(maciekGPParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





