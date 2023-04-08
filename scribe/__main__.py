import Lexer
import Parser
import Interpreter

def print_error(code, error):
    index_of_first_character = error.location.index_of_first_character
    index_of_last_character = error.location.index_of_last_character
    length = (index_of_last_character + 1) - index_of_first_character
    print(code)
    arrow_string = (' ' * index_of_first_character) + ('^' * length)
    print(arrow_string)
    print(error)


print('Scribe')
while True:
    print()
    code = input('> ')
    print()

    lexer = Lexer.Lexer(code)
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