import Token
import Error
import contants

class Lexer:
    def __init__(self, code):
        self.code = code
        self.index = 0
        self.character = code[0]
        self.tokens = []
        self.error = None

    def advance(self):
        self.index += 1
        if self.index < len(self.code):
            self.character = self.code[self.index]
        else:
            self.character = None

    def lex(self):
        while self.character != None:
            if self.error:
                break
            if self.character == '+':
                self.tokens.append(Token.Plus_Token())
                self.advance()
            elif self.character == '-':
                self.tokens.append(Token.Minus_Token())
                self.advance()
            elif self.character == '*':
                self.tokens.append(Token.Multiply_Token())
                self.advance()
            elif self.character == '/':
                self.tokens.append(Token.Divide_Token())
                self.advance()
            elif self.character == '(':
                self.tokens.append(Token.Left_Parenthesis_Token())
                self.advance()
            elif self.character == ')':
                self.tokens.append(Token.Right_Parenthesis_Token())
                self.advance()
            elif self.character == '#':
                self.advance()
                self.lex_integer_or_float()
            elif self.character in ' /t':
                self.advance()
            else:
                self.error = Error.Illegal_Character_Error(self.character)
        self.tokens.append(Token.EOF_Token())
        return self.tokens, self.error
    
    def lex_integer_or_float(self):
        number = ''
        while self.character != None and self.character in contants.base10_digits + '.' + '-':
            number += self.character
            self.advance()
        if '.' in number:
            try:
                number = float(number)
            except:
                self.error = Error.Illegal_Character_Error(self.character)
            else:
                self.tokens.append(Token.Float_Token(number))
        else:
            try:
                number = int(number)
            except:
                self.error = Error.Illegal_Character_Error(self.character)
            else:
                self.tokens.append(Token.Integer_Token(number))