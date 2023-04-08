import Token
import Error
import Location

class Lexer:
    def __init__(self, code, line_number, file_name):
        self.code = code
        self.line_number = line_number
        self.file_name = file_name
        self.index = 0
        self.character = code[0]
        self.error = None

    def advance(self):
        self.index += 1
        if self.index < len(self.code):
            self.character = self.code[self.index]
        else:
            self.character = None

    def lex(self):
        tokens = []
        while self.character != None:
            if self.error:
                break
            if self.character == '+':
                tokens.append(Token.Plus_Token(Location.Location(self.index, self.index + 1, self.line_number, self.file_name)))
                self.advance()
            elif self.character == '-':
                tokens.append(Token.Minus_Token(Location.Location(self.index, self.index + 1, self.line_number, self.file_name)))
                self.advance()
            elif self.character == '*':
                tokens.append(Token.Multiply_Token(Location.Location(self.index, self.index + 1, self.line_number, self.file_name)))
                self.advance()
            elif self.character == '/':
                tokens.append(Token.Divide_Token(Location.Location(self.index, self.index + 1, self.line_number, self.file_name)))
                self.advance()
            elif self.character == '(':
                tokens.append(Token.Left_Parenthesis_Token(Location.Location(self.index, self.index + 1, self.line_number, self.file_name)))
                self.advance()
            elif self.character == ')':
                tokens.append(Token.Right_Parenthesis_Token(Location.Location(self.index, self.index + 1, self.line_number, self.file_name)))
                self.advance()
            elif self.character == '#':
                tokens.append(self.lex_integer_or_float())
            elif self.character in ' /t':
                self.advance()
            else:
                self.error = Error.Illegal_Character_Error(self.character, Location.Location(self.index, self.index + 1, self.line_number, self.file_name))
        tokens.append(Token.EOF_Token(Location.Location(self.index, self.index + 1, self.line_number, self.file_name)))
        return tokens, self.error
    
    def lex_integer_or_float(self):
        left_bound = self.index
        self.advance()
        number = ''
        if self.character == '-':
            number += self.character
            self.advance()
        while self.character != None and self.character in '0123456789.' and self.error == None:
            if self.character == '.' and '.' in number:
                self.error = Error.Illegal_Character_Error(self.character, Location.Location(self.index, self.index + 1, self.line_number, self.file_name))
            else:
                number += self.character
                self.advance()
        if self.error:
            return None
        elif len(number) == 0:
            self.error = Error.Illegal_Character_Error(self.character, Location.Location(self.index, self.index + 1, self.line_number, self.file_name))
        else:
            if '.' in number:
                return Token.Float_Token(float(number), Location.Location(left_bound, self.index, self.line_number, self.file_name))
            else:
                return Token.Integer_Token(int(number), Location.Location(left_bound, self.index, self.line_number, self.file_name))