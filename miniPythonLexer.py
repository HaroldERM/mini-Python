# Generated from C:/Users/harol/PycharmProjects/mini-Python\miniPython.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from miniPythonParser import miniPythonParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u0098\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\7\25z\n\25\f\25\16\25}\13\25\3\26\3\26\3\26\7\26")
        buf.write("\u0082\n\26\f\26\16\26\u0085\13\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\5\31\u008c\n\31\3\31\3\31\7\31\u0090\n\31\f\31\16")
        buf.write("\31\u0093\13\31\3\32\3\32\3\32\3\32\2\2\33\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\2/\2\61\30\63\31\3")
        buf.write("\2\6\3\2\62;\3\2c|\4\2\13\13\"\"\6\2\13\f\17\17\"\"--")
        buf.write("\2\u009a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\3\65\3\2\2\2\5\67\3\2\2\2\7:")
        buf.write("\3\2\2\2\t<\3\2\2\2\13>\3\2\2\2\r@\3\2\2\2\17B\3\2\2\2")
        buf.write("\21D\3\2\2\2\23F\3\2\2\2\25I\3\2\2\2\27N\3\2\2\2\31S\3")
        buf.write("\2\2\2\33Y\3\2\2\2\35\\\3\2\2\2\37`\3\2\2\2!c\3\2\2\2")
        buf.write("#i\3\2\2\2%m\3\2\2\2\'s\3\2\2\2)w\3\2\2\2+~\3\2\2\2-\u0086")
        buf.write("\3\2\2\2/\u0088\3\2\2\2\61\u008b\3\2\2\2\63\u0094\3\2")
        buf.write("\2\2\65\66\7=\2\2\66\4\3\2\2\2\678\7<\2\289\7?\2\29\6")
        buf.write("\3\2\2\2:;\7*\2\2;\b\3\2\2\2<=\7+\2\2=\n\3\2\2\2>?\7\u0080")
        buf.write("\2\2?\f\3\2\2\2@A\7<\2\2A\16\3\2\2\2BC\7-\2\2C\20\3\2")
        buf.write("\2\2DE\7,\2\2E\22\3\2\2\2FG\7k\2\2GH\7h\2\2H\24\3\2\2")
        buf.write("\2IJ\7v\2\2JK\7j\2\2KL\7g\2\2LM\7p\2\2M\26\3\2\2\2NO\7")
        buf.write("g\2\2OP\7n\2\2PQ\7u\2\2QR\7g\2\2R\30\3\2\2\2ST\7y\2\2")
        buf.write("TU\7j\2\2UV\7k\2\2VW\7n\2\2WX\7g\2\2X\32\3\2\2\2YZ\7f")
        buf.write("\2\2Z[\7q\2\2[\34\3\2\2\2\\]\7n\2\2]^\7g\2\2^_\7v\2\2")
        buf.write("_\36\3\2\2\2`a\7k\2\2ab\7p\2\2b \3\2\2\2cd\7d\2\2de\7")
        buf.write("g\2\2ef\7i\2\2fg\7k\2\2gh\7p\2\2h\"\3\2\2\2ij\7g\2\2j")
        buf.write("k\7p\2\2kl\7f\2\2l$\3\2\2\2mn\7e\2\2no\7q\2\2op\7p\2\2")
        buf.write("pq\7u\2\2qr\7v\2\2r&\3\2\2\2st\7x\2\2tu\7c\2\2uv\7t\2")
        buf.write("\2v(\3\2\2\2w{\5-\27\2xz\5-\27\2yx\3\2\2\2z}\3\2\2\2{")
        buf.write("y\3\2\2\2{|\3\2\2\2|*\3\2\2\2}{\3\2\2\2~\u0083\5/\30\2")
        buf.write("\177\u0082\5/\30\2\u0080\u0082\5-\27\2\u0081\177\3\2\2")
        buf.write("\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0083\u0084\3\2\2\2\u0084,\3\2\2\2\u0085\u0083")
        buf.write("\3\2\2\2\u0086\u0087\t\2\2\2\u0087.\3\2\2\2\u0088\u0089")
        buf.write("\t\3\2\2\u0089\60\3\2\2\2\u008a\u008c\7\17\2\2\u008b\u008a")
        buf.write("\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\u0091\7\f\2\2\u008e\u0090\t\4\2\2\u008f\u008e\3\2\2\2")
        buf.write("\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3")
        buf.write("\2\2\2\u0092\62\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095")
        buf.write("\t\5\2\2\u0095\u0096\3\2\2\2\u0096\u0097\b\32\2\2\u0097")
        buf.write("\64\3\2\2\2\b\2{\u0081\u0083\u008b\u0091\3\b\2\2")
        return buf.getvalue()


class miniPythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PyCOMA = 1
    ASIGN = 2
    PIZQ = 3
    PDER = 4
    VIR = 5
    DOSPUNT = 6
    MAS = 7
    MULT = 8
    IF = 9
    THEN = 10
    ELSE = 11
    WHILE = 12
    DO = 13
    LET = 14
    IN = 15
    BEGIN = 16
    END = 17
    CONST = 18
    VAR = 19
    NUM = 20
    ID = 21
    NEWLINE = 22
    WS = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':='", "'('", "')'", "'~'", "':'", "'+'", "'*'", "'if'", 
            "'then'", "'else'", "'while'", "'do'", "'let'", "'in'", "'begin'", 
            "'end'", "'const'", "'var'" ]

    symbolicNames = [ "<INVALID>",
            "PyCOMA", "ASIGN", "PIZQ", "PDER", "VIR", "DOSPUNT", "MAS", 
            "MULT", "IF", "THEN", "ELSE", "WHILE", "DO", "LET", "IN", "BEGIN", 
            "END", "CONST", "VAR", "NUM", "ID", "NEWLINE", "WS" ]

    ruleNames = [ "PyCOMA", "ASIGN", "PIZQ", "PDER", "VIR", "DOSPUNT", "MAS", 
                  "MULT", "IF", "THEN", "ELSE", "WHILE", "DO", "LET", "IN", 
                  "BEGIN", "END", "CONST", "VAR", "NUM", "ID", "DIGIT", 
                  "LETTER", "NEWLINE", "WS" ]

    grammarFileName = "miniPython.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class miniPythonDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: miniPythonLexer = lexer

        def pull_token(self):
            return super(miniPythonLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.miniPythonDenter(self, self.NEWLINE, miniPythonParser.INDENT, miniPythonParser.DEDENT, False)
        return self.denter.next_token()


