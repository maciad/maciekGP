# Generated from ./maciekGP.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,25,139,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,1,
        1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,
        1,15,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,20,1,20,
        1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,5,22,121,8,22,10,22,12,22,
        124,9,22,1,22,1,22,1,23,4,23,129,8,23,11,23,12,23,130,1,23,1,23,
        1,24,4,24,136,8,24,11,24,12,24,137,0,0,25,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,
        35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,1,0,3,2,0,10,10,
        13,13,3,0,9,10,13,13,32,32,1,0,48,57,141,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,
        25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,
        35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,
        45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,1,51,1,0,0,0,3,53,1,0,0,0,5,
        56,1,0,0,0,7,58,1,0,0,0,9,60,1,0,0,0,11,65,1,0,0,0,13,67,1,0,0,0,
        15,69,1,0,0,0,17,74,1,0,0,0,19,80,1,0,0,0,21,87,1,0,0,0,23,89,1,
        0,0,0,25,91,1,0,0,0,27,93,1,0,0,0,29,95,1,0,0,0,31,97,1,0,0,0,33,
        100,1,0,0,0,35,103,1,0,0,0,37,105,1,0,0,0,39,107,1,0,0,0,41,110,
        1,0,0,0,43,113,1,0,0,0,45,116,1,0,0,0,47,128,1,0,0,0,49,135,1,0,
        0,0,51,52,5,61,0,0,52,2,1,0,0,0,53,54,5,105,0,0,54,55,5,102,0,0,
        55,4,1,0,0,0,56,57,5,40,0,0,57,6,1,0,0,0,58,59,5,41,0,0,59,8,1,0,
        0,0,60,61,5,101,0,0,61,62,5,108,0,0,62,63,5,115,0,0,63,64,5,101,
        0,0,64,10,1,0,0,0,65,66,5,123,0,0,66,12,1,0,0,0,67,68,5,125,0,0,
        68,14,1,0,0,0,69,70,5,108,0,0,70,71,5,111,0,0,71,72,5,111,0,0,72,
        73,5,112,0,0,73,16,1,0,0,0,74,75,5,112,0,0,75,76,5,114,0,0,76,77,
        5,105,0,0,77,78,5,110,0,0,78,79,5,116,0,0,79,18,1,0,0,0,80,81,5,
        114,0,0,81,82,5,101,0,0,82,83,5,97,0,0,83,84,5,100,0,0,84,85,5,40,
        0,0,85,86,5,41,0,0,86,20,1,0,0,0,87,88,5,42,0,0,88,22,1,0,0,0,89,
        90,5,47,0,0,90,24,1,0,0,0,91,92,5,43,0,0,92,26,1,0,0,0,93,94,5,45,
        0,0,94,28,1,0,0,0,95,96,5,37,0,0,96,30,1,0,0,0,97,98,5,61,0,0,98,
        99,5,61,0,0,99,32,1,0,0,0,100,101,5,33,0,0,101,102,5,61,0,0,102,
        34,1,0,0,0,103,104,5,60,0,0,104,36,1,0,0,0,105,106,5,62,0,0,106,
        38,1,0,0,0,107,108,5,60,0,0,108,109,5,61,0,0,109,40,1,0,0,0,110,
        111,5,62,0,0,111,112,5,61,0,0,112,42,1,0,0,0,113,114,5,120,0,0,114,
        115,5,95,0,0,115,44,1,0,0,0,116,117,5,47,0,0,117,118,5,47,0,0,118,
        122,1,0,0,0,119,121,8,0,0,0,120,119,1,0,0,0,121,124,1,0,0,0,122,
        120,1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,122,1,0,0,0,125,
        126,6,22,0,0,126,46,1,0,0,0,127,129,7,1,0,0,128,127,1,0,0,0,129,
        130,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,
        133,6,23,0,0,133,48,1,0,0,0,134,136,7,2,0,0,135,134,1,0,0,0,136,
        137,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,50,1,0,0,0,4,0,122,
        130,137,1,6,0,0
    ]

class maciekGPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    COMMENT = 23
    WS = 24
    INT = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'if'", "'('", "')'", "'else'", "'{'", "'}'", "'loop'", 
            "'print'", "'read()'", "'*'", "'/'", "'+'", "'-'", "'%'", "'=='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "'x_'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "WS", "INT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "COMMENT", "WS", "INT" ]

    grammarFileName = "maciekGP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


