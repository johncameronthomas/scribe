import Lexer
import Parser

while True:
    code = input('> ')

    lexer = Lexer.Lexer(code)
    tokens, error = lexer.lex()
    parser = Parser.Parser(tokens)
    tree = parser.parse()
    print(tree)