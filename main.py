from miniPythonLexer import *
from miniPythonParser import *
from antlr4 import *

def main():
    input = FileStream('test.txt')
    lexer = miniPythonLexer(input)
    stream = CommonTokenStream(lexer)
    parser = miniPythonParser(stream)
    tree = parser.program()

if __name__ == '__main__':
    main()