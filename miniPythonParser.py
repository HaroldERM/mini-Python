# Generated from C:/Users/harol/PycharmProjects/mini-Python\miniPython.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\7")
        buf.write("\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4)\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4@\n\4\3\5\3")
        buf.write("\5\3\5\7\5E\n\5\f\5\16\5H\13\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6R\n\6\3\7\3\7\3\b\3\b\3\b\3\b\7\bZ\n\b\f\b")
        buf.write("\16\b]\13\b\3\t\3\t\3\t\3\t\3\t\3\t\5\te\n\t\3\n\3\n\3")
        buf.write("\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3\2\t\n\2j\2\24\3\2")
        buf.write("\2\2\4\31\3\2\2\2\6?\3\2\2\2\bA\3\2\2\2\nQ\3\2\2\2\fS")
        buf.write("\3\2\2\2\16U\3\2\2\2\20d\3\2\2\2\22f\3\2\2\2\24\25\7\32")
        buf.write("\2\2\25\26\5\6\4\2\26\27\7\30\2\2\27\30\7\33\2\2\30\3")
        buf.write("\3\2\2\2\31\36\5\6\4\2\32\33\7\3\2\2\33\35\5\6\4\2\34")
        buf.write("\32\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37")
        buf.write("\5\3\2\2\2 \36\3\2\2\2!(\7\27\2\2\"#\7\4\2\2#)\5\16\b")
        buf.write("\2$%\7\5\2\2%&\5\16\b\2&\'\7\6\2\2\')\3\2\2\2(\"\3\2\2")
        buf.write("\2($\3\2\2\2)@\3\2\2\2*+\7\13\2\2+,\5\16\b\2,-\7\f\2\2")
        buf.write("-.\5\6\4\2./\7\r\2\2/\60\5\6\4\2\60@\3\2\2\2\61\62\7\16")
        buf.write("\2\2\62\63\5\16\b\2\63\64\7\17\2\2\64\65\5\6\4\2\65@\3")
        buf.write("\2\2\2\66\67\7\20\2\2\678\5\b\5\289\7\21\2\29:\5\6\4\2")
        buf.write(":@\3\2\2\2;<\7\22\2\2<=\5\4\3\2=>\7\23\2\2>@\3\2\2\2?")
        buf.write("!\3\2\2\2?*\3\2\2\2?\61\3\2\2\2?\66\3\2\2\2?;\3\2\2\2")
        buf.write("@\7\3\2\2\2AF\5\n\6\2BC\7\3\2\2CE\5\n\6\2DB\3\2\2\2EH")
        buf.write("\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\t\3\2\2\2HF\3\2\2\2IJ\7")
        buf.write("\24\2\2JK\7\27\2\2KL\7\7\2\2LR\5\16\b\2MN\7\25\2\2NO\7")
        buf.write("\27\2\2OP\7\b\2\2PR\5\f\7\2QI\3\2\2\2QM\3\2\2\2R\13\3")
        buf.write("\2\2\2ST\7\27\2\2T\r\3\2\2\2U[\5\20\t\2VW\5\22\n\2WX\5")
        buf.write("\20\t\2XZ\3\2\2\2YV\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2")
        buf.write("\2\2\\\17\3\2\2\2][\3\2\2\2^e\7\26\2\2_e\7\27\2\2`a\7")
        buf.write("\5\2\2ab\5\16\b\2bc\7\6\2\2ce\3\2\2\2d^\3\2\2\2d_\3\2")
        buf.write("\2\2d`\3\2\2\2e\21\3\2\2\2fg\t\2\2\2g\23\3\2\2\2\t\36")
        buf.write("(?FQ[d")
        return buf.getvalue()


class miniPythonParser ( Parser ):

    grammarFileName = "miniPython.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "':='", "'('", "')'", "'~'", "':'", 
                     "'+'", "'*'", "'if'", "'then'", "'else'", "'while'", 
                     "'do'", "'let'", "'in'", "'begin'", "'end'", "'const'", 
                     "'var'" ]

    symbolicNames = [ "<INVALID>", "PyCOMA", "ASIGN", "PIZQ", "PDER", "VIR", 
                      "DOSPUNT", "MAS", "MULT", "IF", "THEN", "ELSE", "WHILE", 
                      "DO", "LET", "IN", "BEGIN", "END", "CONST", "VAR", 
                      "NUM", "ID", "NEWLINE", "WS", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_command = 1
    RULE_singleCommand = 2
    RULE_declaration = 3
    RULE_singleDeclaration = 4
    RULE_typedenoter = 5
    RULE_expression = 6
    RULE_primaryExpression = 7
    RULE_operator = 8

    ruleNames =  [ "program", "command", "singleCommand", "declaration", 
                   "singleDeclaration", "typedenoter", "expression", "primaryExpression", 
                   "operator" ]

    EOF = Token.EOF
    PyCOMA=1
    ASIGN=2
    PIZQ=3
    PDER=4
    VIR=5
    DOSPUNT=6
    MAS=7
    MULT=8
    IF=9
    THEN=10
    ELSE=11
    WHILE=12
    DO=13
    LET=14
    IN=15
    BEGIN=16
    END=17
    CONST=18
    VAR=19
    NUM=20
    ID=21
    NEWLINE=22
    WS=23
    INDENT=24
    DEDENT=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(miniPythonParser.INDENT, 0)

        def singleCommand(self):
            return self.getTypedRuleContext(miniPythonParser.SingleCommandContext,0)


        def NEWLINE(self):
            return self.getToken(miniPythonParser.NEWLINE, 0)

        def DEDENT(self):
            return self.getToken(miniPythonParser.DEDENT, 0)

        def getRuleIndex(self):
            return miniPythonParser.RULE_program




    def program(self):

        localctx = miniPythonParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(miniPythonParser.INDENT)
            self.state = 19
            self.singleCommand()
            self.state = 20
            self.match(miniPythonParser.NEWLINE)
            self.state = 21
            self.match(miniPythonParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniPythonParser.SingleCommandContext)
            else:
                return self.getTypedRuleContext(miniPythonParser.SingleCommandContext,i)


        def PyCOMA(self, i:int=None):
            if i is None:
                return self.getTokens(miniPythonParser.PyCOMA)
            else:
                return self.getToken(miniPythonParser.PyCOMA, i)

        def getRuleIndex(self):
            return miniPythonParser.RULE_command




    def command(self):

        localctx = miniPythonParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.singleCommand()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miniPythonParser.PyCOMA:
                self.state = 24
                self.match(miniPythonParser.PyCOMA)
                self.state = 25
                self.singleCommand()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(miniPythonParser.ID, 0)

        def ASIGN(self):
            return self.getToken(miniPythonParser.ASIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(miniPythonParser.ExpressionContext,0)


        def PIZQ(self):
            return self.getToken(miniPythonParser.PIZQ, 0)

        def PDER(self):
            return self.getToken(miniPythonParser.PDER, 0)

        def IF(self):
            return self.getToken(miniPythonParser.IF, 0)

        def THEN(self):
            return self.getToken(miniPythonParser.THEN, 0)

        def singleCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniPythonParser.SingleCommandContext)
            else:
                return self.getTypedRuleContext(miniPythonParser.SingleCommandContext,i)


        def ELSE(self):
            return self.getToken(miniPythonParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(miniPythonParser.WHILE, 0)

        def DO(self):
            return self.getToken(miniPythonParser.DO, 0)

        def LET(self):
            return self.getToken(miniPythonParser.LET, 0)

        def declaration(self):
            return self.getTypedRuleContext(miniPythonParser.DeclarationContext,0)


        def IN(self):
            return self.getToken(miniPythonParser.IN, 0)

        def BEGIN(self):
            return self.getToken(miniPythonParser.BEGIN, 0)

        def command(self):
            return self.getTypedRuleContext(miniPythonParser.CommandContext,0)


        def END(self):
            return self.getToken(miniPythonParser.END, 0)

        def getRuleIndex(self):
            return miniPythonParser.RULE_singleCommand




    def singleCommand(self):

        localctx = miniPythonParser.SingleCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_singleCommand)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miniPythonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(miniPythonParser.ID)
                self.state = 38
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [miniPythonParser.ASIGN]:
                    self.state = 32
                    self.match(miniPythonParser.ASIGN)
                    self.state = 33
                    self.expression()
                    pass
                elif token in [miniPythonParser.PIZQ]:
                    self.state = 34
                    self.match(miniPythonParser.PIZQ)
                    self.state = 35
                    self.expression()
                    self.state = 36
                    self.match(miniPythonParser.PDER)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [miniPythonParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(miniPythonParser.IF)
                self.state = 41
                self.expression()
                self.state = 42
                self.match(miniPythonParser.THEN)
                self.state = 43
                self.singleCommand()
                self.state = 44
                self.match(miniPythonParser.ELSE)
                self.state = 45
                self.singleCommand()
                pass
            elif token in [miniPythonParser.WHILE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.match(miniPythonParser.WHILE)
                self.state = 48
                self.expression()
                self.state = 49
                self.match(miniPythonParser.DO)
                self.state = 50
                self.singleCommand()
                pass
            elif token in [miniPythonParser.LET]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.match(miniPythonParser.LET)
                self.state = 53
                self.declaration()
                self.state = 54
                self.match(miniPythonParser.IN)
                self.state = 55
                self.singleCommand()
                pass
            elif token in [miniPythonParser.BEGIN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.match(miniPythonParser.BEGIN)
                self.state = 58
                self.command()
                self.state = 59
                self.match(miniPythonParser.END)
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


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniPythonParser.SingleDeclarationContext)
            else:
                return self.getTypedRuleContext(miniPythonParser.SingleDeclarationContext,i)


        def PyCOMA(self, i:int=None):
            if i is None:
                return self.getTokens(miniPythonParser.PyCOMA)
            else:
                return self.getToken(miniPythonParser.PyCOMA, i)

        def getRuleIndex(self):
            return miniPythonParser.RULE_declaration




    def declaration(self):

        localctx = miniPythonParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.singleDeclaration()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miniPythonParser.PyCOMA:
                self.state = 64
                self.match(miniPythonParser.PyCOMA)
                self.state = 65
                self.singleDeclaration()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(miniPythonParser.CONST, 0)

        def ID(self):
            return self.getToken(miniPythonParser.ID, 0)

        def VIR(self):
            return self.getToken(miniPythonParser.VIR, 0)

        def expression(self):
            return self.getTypedRuleContext(miniPythonParser.ExpressionContext,0)


        def VAR(self):
            return self.getToken(miniPythonParser.VAR, 0)

        def DOSPUNT(self):
            return self.getToken(miniPythonParser.DOSPUNT, 0)

        def typedenoter(self):
            return self.getTypedRuleContext(miniPythonParser.TypedenoterContext,0)


        def getRuleIndex(self):
            return miniPythonParser.RULE_singleDeclaration




    def singleDeclaration(self):

        localctx = miniPythonParser.SingleDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_singleDeclaration)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miniPythonParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(miniPythonParser.CONST)
                self.state = 72
                self.match(miniPythonParser.ID)
                self.state = 73
                self.match(miniPythonParser.VIR)
                self.state = 74
                self.expression()
                pass
            elif token in [miniPythonParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(miniPythonParser.VAR)
                self.state = 76
                self.match(miniPythonParser.ID)
                self.state = 77
                self.match(miniPythonParser.DOSPUNT)
                self.state = 78
                self.typedenoter()
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


    class TypedenoterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(miniPythonParser.ID, 0)

        def getRuleIndex(self):
            return miniPythonParser.RULE_typedenoter




    def typedenoter(self):

        localctx = miniPythonParser.TypedenoterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typedenoter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(miniPythonParser.ID)
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

        def primaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniPythonParser.PrimaryExpressionContext)
            else:
                return self.getTypedRuleContext(miniPythonParser.PrimaryExpressionContext,i)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniPythonParser.OperatorContext)
            else:
                return self.getTypedRuleContext(miniPythonParser.OperatorContext,i)


        def getRuleIndex(self):
            return miniPythonParser.RULE_expression




    def expression(self):

        localctx = miniPythonParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.primaryExpression()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miniPythonParser.MAS or _la==miniPythonParser.MULT:
                self.state = 84
                self.operator()
                self.state = 85
                self.primaryExpression()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(miniPythonParser.NUM, 0)

        def ID(self):
            return self.getToken(miniPythonParser.ID, 0)

        def PIZQ(self):
            return self.getToken(miniPythonParser.PIZQ, 0)

        def expression(self):
            return self.getTypedRuleContext(miniPythonParser.ExpressionContext,0)


        def PDER(self):
            return self.getToken(miniPythonParser.PDER, 0)

        def getRuleIndex(self):
            return miniPythonParser.RULE_primaryExpression




    def primaryExpression(self):

        localctx = miniPythonParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primaryExpression)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miniPythonParser.NUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(miniPythonParser.NUM)
                pass
            elif token in [miniPythonParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(miniPythonParser.ID)
                pass
            elif token in [miniPythonParser.PIZQ]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(miniPythonParser.PIZQ)
                self.state = 95
                self.expression()
                self.state = 96
                self.match(miniPythonParser.PDER)
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


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAS(self):
            return self.getToken(miniPythonParser.MAS, 0)

        def MULT(self):
            return self.getToken(miniPythonParser.MULT, 0)

        def getRuleIndex(self):
            return miniPythonParser.RULE_operator




    def operator(self):

        localctx = miniPythonParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not(_la==miniPythonParser.MAS or _la==miniPythonParser.MULT):
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





