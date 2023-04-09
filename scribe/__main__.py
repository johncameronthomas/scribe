import Lexer
import Parser
import Interpreter
import Context

context = Context.Context('root', None)

print('Scribe')
while True:
    code = input('> ')

    lexer = Lexer.Lexer(code, 0, 'Command Line Interpreter')
    tokens, error = lexer.lex()
    if error:
        print()
        error.print_error(code)
        print()
        continue
    parser = Parser.Parser(tokens)
    node, error = parser.parse()
    if error:
        print()
        error.print_error(code)
        print()
        continue
    interpreter = Interpreter.Interpreter(node, context)
    result, error = interpreter.interpret()
    if error:
        print()
        error.print_error(code)
        print()
        continue
    print(result)
    print()