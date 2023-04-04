import Lexer

code = '-1.3 * 233.34324'
lexer = Lexer.Lexer(code)
tokens, error = lexer.make_tokens()

print(tokens, error)
