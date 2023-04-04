import Error
import Token

class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = -1
        self.character = None

    def advance(self):
        self.position += 1
        if self.position < len(self.code):
            self.character = self.code[self.position]
        else:
            self.character = None

    def make_number_token(self):
        number = ''
        includes_dot = False
        while self.character != None and self.character in '0123456789.':
            if self.character == '.':
                if includes_dot:
                    break
                else:
                    includes_dot = True
                    number += self.character
            else:
                number += self.character
            self.advance()
        if includes_dot:
            return Token.Float(float(number))
        else:
            return Token.Integer(int(number))

    def make_tokens(self):
        self.advance()
        tokens = []
        while self.character != None:
            if self.character in ' \t':
                self.advance()
            elif self.character in '0123456789':
                tokens.append(self.make_number_token())
            elif self.character == '+':
                tokens.append(Token.Plus())
                self.advance()
            elif self.character == '-':
                tokens.append(Token.Minus())
                self.advance()
            elif self.character == '*':
                tokens.append(Token.Multiply())
                self.advance()
            elif self.character == '/':
                tokens.append(Token.Divide())
                self.advance()
            elif self.character == '(':
                tokens.append(Token.Left_Parenthesis())
                self.advance()
            elif self.character == ')':
                tokens.append(Token.Right_Parenthesis())
                self.advance()
            else:
                return tokens, Error.Illegal_Character(self.character)
        return tokens, None