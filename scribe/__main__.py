import Lexer
import Parser
import Interpreter

def print_error(code, error):
    left_bound = error.location.left_bound
    length = error.location.right_bound - left_bound
    arrow_string = (' ' * left_bound) + ('^' * length)
    print()
    print("Line {} in file '{}'.".format(error.location.line_number, error.location.file_name))
    print(code)
    print(arrow_string)
    print('{}: {}'.format(type(error).__name__, error.message))
    print()

print('Scribe')
while True:
    code = input('> ')

    lexer = Lexer.Lexer(code, 0, 'Command Line Interpreter')
    tokens, error = lexer.lex()
    if error:
        print_error(code, error)
        continue

    parser = Parser.Parser(tokens)
    node, error = parser.parse()
    if error:
        print_error(code, error)
        continue

    interpreter = Interpreter.Interpreter(node)
    result, error = interpreter.interpret()
    if error:
        print_error(code, error)
        continue
    print(result)