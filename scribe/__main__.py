from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
import Context

context = Context.Context('root', None)

print('Scribe')
while True:
    code = input('> ')

    lexer = Lexer(code, 0, 'Command Line Interpreter')
    tokens, error = lexer.lex()
    if error:
        print()
        error.print_error(code)
        print()
        continue
    parser = Parser(tokens)
    tree, error = parser.parse()
    if error:
        print(tree)
        print()
        error.print_error(code)
        print()
        continue
    print(tree)