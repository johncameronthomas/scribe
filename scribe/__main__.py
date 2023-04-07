import Lexer
import Parser

while True:
    print()
    code = input('Scribe>')
    print()

    lexer = Lexer.Lexer(code)
    tokens, error = lexer.lex()
    if error:
        print(error)
        continue
    parser = Parser.Parser(tokens)
    tree, error = parser.parse()
    if error:
        print(error)
        continue
    print(tree)