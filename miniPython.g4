
grammar miniPython;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from generated.miniPythonParser import miniPythonParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: miniPythonLexer = lexer

    def pull_token(self):
        return super(miniPythonLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NEWLINE, miniPythonParser.INDENT, miniPythonParser.DEDENT, False)
    return self.denter.next_token()
}


//parser rules
program: statement+                                                                                                     #programAST;
statement:
          defStatement                                                                                                  #defS
        | ifStatement                                                                                                   #ifS
        | returnStatement                                                                                               #returnS
        | printStatement                                                                                                #printS
        | whileStatement                                                                                                #whileS
        | forStatement                                                                                                  #forS
        | assignStatement                                                                                               #assignS
        | functionCallStatement                                                                                         #functionCallS
        | expressionStatement                                                                                           #expressionS;
defStatement: DEF IDENTIFIER PIZQ argList PDER DOSPUNTOS sequence                                                       #defStatementAST;
argList: (IDENTIFIER moreArgs)?                                                                                         #argListAST;
moreArgs: (COMA IDENTIFIER)*                                                                                            #moreArgsAST;
ifStatement: IF expression DOSPUNTOS sequence ELSE DOSPUNTOS sequence                                                   #ifStatementAST;
whileStatement: WHILE expression DOSPUNTOS sequence                                                                     #whileStatementAST;
forStatement: FOR expression IN expressionList DOSPUNTOS sequence                                                       #forStatementAST;
returnStatement: RETURN expression NEWLINE                                                                              #returnStatementAST;
printStatement: PRINT expression NEWLINE                                                                                #printStatementAST;
assignStatement: IDENTIFIER ASSIGN expression NEWLINE                                                                   #assignStatementAST;
expressionStatement: expressionList NEWLINE                                                                             #expressionStatementAST;
functionCallStatement: primitiveExpression PIZQ expressionList PDER NEWLINE                                             #functionCallStatementAST;
sequence: INDENT moreStatements DEDENT                                                                                  #sequenceAST;
moreStatements: statement+                                                                                              #moreStatementsAST;
expression: additionExpression comparison                                                                               #expressionAST;
additionExpression: multiplicationExpression additionFactor                                                             #additionExpressionAST;
comparison: ((MENORQUE | MAYORQUE | MENORIGUALQUE | MAYORIGUALQUE | IGUALQUE) additionExpression)*                      #comparisonAST;
additionFactor: ((SUM | SUB) multiplicationExpression)*                                                                 #additionFactorAST;
multiplicationExpression: elementExpression multiplicationFactor                                                        #multiplicationExpressionAST;
multiplicationFactor: ((MUL | DIV) elementExpression)*                                                                  #multiplicationFactorAST;
elementExpression: primitiveExpression elementAccess                                                                    #elementExpressionAST;
elementAccess: (CIZQ expression CDER)*                                                                                  #elementAccessAST;
expressionList: (expression moreExpressions)?                                                                           #expressionListAST;
moreExpressions: (COMA expression)*                                                                                     #moreExpressionsAST;
primitiveExpression:
                    NUMBER                                                                                              #numberPE
                  | STRING                                                                                              #stringPE
                  | IDENTIFIER (PIZQ expressionList PDER)?                                                              #idCallPE
                  | PIZQ expression PDER                                                                                #exprPE
                  | listExpression                                                                                      #listExprPE
                  | LEN PIZQ expression PDER                                                                            #lenExprPE;
listExpression: CIZQ expressionList CDER                                                                                #listExpressionAST;

/*
 * lexer rules
 */

//simbols
ASSIGN        : '=';
PIZQ          : '(';
PDER          : ')';
CIZQ          : '[';
CDER          : ']';
COMA          : ',';
DOSPUNTOS     : ':';
MENORQUE      : '<';
MAYORQUE      : '>';
MENORIGUALQUE : '<=';
MAYORIGUALQUE : '>=';
IGUALQUE      : '==';
SUM           : '+';
SUB           : '-';
MUL           : '*';
DIV           : '/';

//reserved words
IF     : 'if';
ELSE   : 'else';
WHILE  : 'while';
FOR    : 'for';
IN     : 'in';
DEF    : 'def';
PRINT  : 'print';
RETURN : 'return';
LEN    : 'len';

//other tokens
IDENTIFIER : ID_START ID_CONTINUE* ;
NUMBER     : INTEGER | FLOAT ;
STRING     : '"' .*? '"'  ;
INTEGER    : NON_ZERO_DIGIT DIGIT* | PIZQ SUB NON_ZERO_DIGIT DIGIT* PDER | '0';
FLOAT      : POINT_FLOAT | PIZQ SUB POINT_FLOAT PDER ;

NEWLINE      : ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' ' with '\t'*
SKIP_        : ( WS | COMMENT | LONG_COMMENT ) -> skip ;
UNKNOWN_CHAR : . ;

//fragments
/// IDENTIFIER          ::= ID_START ID_CONTINUE* ;
fragment ID_START       : '_' | [A-Z] | [a-z] ;
fragment ID_CONTINUE    : ID_START | [0-9] ;

/// nonzerodigit        ::=  "1"..."9"
fragment NON_ZERO_DIGIT : [1-9] ;

/// digit               ::=  "0"..."9"
fragment DIGIT          : [0-9] ;

/// pointfloat          ::=  (number !=0) digit* fraction | '0' fraction
fragment POINT_FLOAT    : NON_ZERO_DIGIT DIGIT* FRACTION | '0' FRACTION;

/// fraction            ::=  "." digit+
fragment FRACTION       : '.' DIGIT+ ;

/// fragments to skip_
fragment WS             : [ +\r\n\t] ;
fragment COMMENT        : '#' ~[\r\n\f]* ;
fragment LONG_COMMENT   :  '"""' .*? '"""' ;