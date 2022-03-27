import sys
sys.path.append('./generated')
from generated.miniPythonLexer import *
from generated.miniPythonParser import *
from antlr4 import *

def main():
    input = FileStream('test.txt')
    lexer = miniPythonLexer(input)
    stream = CommonTokenStream(lexer)
    parser = miniPythonParser(stream)
    tree = parser.program()

if __name__ == '__main__':
    main()
