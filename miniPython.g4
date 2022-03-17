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

program : INDENT singleCommand NEWLINE DEDENT ; //el DEDENT debe llevar antes un NEWLINE
command : singleCommand (PyCOMA singleCommand)* ;
singleCommand :
        ID ( ASIGN expression | PIZQ expression PDER)
        | IF expression THEN singleCommand
                        ELSE singleCommand
        | WHILE expression DO singleCommand
        | LET declaration IN singleCommand
        | BEGIN command END ;

declaration  : singleDeclaration (PyCOMA singleDeclaration)* ;

singleDeclaration :
            CONST ID VIR expression
    	   | VAR ID DOSPUNT typedenoter ;
typedenoter : ID ;
expression : primaryExpression (operator primaryExpression)* ;
primaryExpression : NUM | ID | PIZQ expression PDER ;
operator : MAS | MULT ; //faltan el resto

//símbolos
PyCOMA : ';';
ASIGN : ':=';
PIZQ : '(';
PDER : ')';
VIR : '~';
DOSPUNT : ':';
MAS : '+';
MULT : '*';
//FALTAN OTROS

//palabras reservadas
IF : 'if';
THEN : 'then';
ELSE : 'else';
WHILE : 'while';
DO : 'do';
LET : 'let';
IN : 'in';
BEGIN : 'begin';
END : 'end';
CONST : 'const';
VAR : 'var';

//otros tokens
NUM : DIGIT DIGIT*;
ID : LETTER (LETTER | DIGIT)*;

fragment DIGIT : [0-9];
fragment LETTER : [a-z];

NEWLINE: ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' '* with '\t'*

WS  :   [ +\r\n\t] -> skip ;