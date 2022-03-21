grammar miniPython;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from miniPythonParser import miniPythonParser
}
@lexer::members {
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
}

program : statement | statement program;
statement : defStatement | ifStatement | returnStatement | printStatement | whileStatement | forStatement | assignStatement | functionCallStatement | expressionStatement;
defStatement : DEF ID PIZQ argList PDER DOSPUNT sequence;
argList : (ID moreArgs)?;
moreArgs : (COMA ID)*;
ifStatement : IF expression DOSPUNT sequence ELSE DOSPUNT sequence;
whileStatement : WHILE expression DOSPUNT sequence;
forStatement : FOR expression IN expressionList DOSPUNT sequence;
returnStatement : RETURN expression NEWLINE;
printStatement : PRINT expression NEWLINE;
assignStatement : ID ASIGN expression NEWLINE;
functionCallStatement : primitiveExpression PIZQ expressionList PDER NEWLINE;
expressionStatement : expressionList NEWLINE;
sequence : INDENT moreStatements DEDENT;
moreStatements : statement moreStatements | statement;
expression : additionExpression comparison;
comparison : ((MENORQUE|MAYORQUE|MENORIGUALQUE|MAYOTIGUALQUE|IGUALQUE) additionExpression)*;
additionExpression : multiplicationExpression additionFactor;
additionFactor : ((SUM|SUB) multiplicationExpression)*;
multiplicationExpression : elementExpression multiplicationFactor;
multiplicationFactor : ((MUL|DIV) elementExpression)*;
elementExpression : primitiveExpression elementAccess;
elementAccess : (CIZQ expression CDER)*;
expressionList : (expression moreExpressions)?;
moreExpressions : (COMA expression)*;
primitiveExpression : INTEGER | FLOAT | CHARCONST | STRING | ID (PIZQ expressionList PDER)? | PIZQ expression PDER | listExpression | LEN PIZQ expression PDER;
listExpression : CIZQ expressionList CDER;

//---------------------------------------------------------------------------------

//símbolos
ASIGN         : '=';
PIZQ          : '(';
PDER          : ')';
CIZQ          : '[';
CDER          : ']';
COMA          : ',';
DOSPUNT       : ':';
MENORQUE      : '<';
MAYORQUE      : '>';
MENORIGUALQUE : '<=';
MAYOTIGUALQUE : '>=';
IGUALQUE      : '==';
SUM           : '+';
SUB           : '-';
MUL           : '*';
DIV           : '/';

//palabras reservadas
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';
IN      : 'in';
DEF     : 'def';
PRINT   : 'print';
RETURN  : 'return';
LEN     : 'len';

//otros tokens
ID        : LETTER (LETTER | DIGIT)*;
INTEGER   : PARTE_ENTERA;
FLOAT     : POINT_FLOAT;
CHARCONST : STRING;
STRING    : ( [rR] | [uU] | [fF] | ( [fF] [rR] ) | ( [rR] [fF] ) )? ( SHORT_STRING | LONG_STRING );

NEWLINE   : ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' '* with '\t'*

// Fragments
fragment DIGIT             : [0-9];
fragment PARTE_ENTERA      : DIGIT+;
fragment FRACTION          : '.' DIGIT+;
fragment LETTER            : [a-zA-Z _];
fragment STRING_PART       : '"'LETTER+'"';
fragment POINT_FLOAT       : PARTE_ENTERA? FRACTION | PARTE_ENTERA '.';



fragment SHORT_STRING      : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f'] )* '\'' | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f"] )* '"';
fragment LONG_STRING       : '\'\'\'' LONG_STRING_ITEM*? '\'\'\'' | '"""' LONG_STRING_ITEM*? '"""';
fragment LONG_STRING_ITEM  : LONG_STRING_CHAR | STRING_ESCAPE_SEQ;
fragment LONG_STRING_CHAR  : ~'\\';
fragment STRING_ESCAPE_SEQ : '\\' . | '\\' NEWLINE;

LINE_COMMENT   : '#' ~[\r\n\f]* -> skip ;
LARGE_COMMENT  : '"""' ~[\r\n\f\t]* '"""' -> skip ;
WS  :   [ +\r\n\t] -> skip ;