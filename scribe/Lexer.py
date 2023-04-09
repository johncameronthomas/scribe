import Token
import Error
import Location
import constants

class Lexer:
    def __init__(self, code, line_number, file_name):
        self.code = code
        self.line_number = line_number
        self.file_name = file_name
        self.index = 0
        self.character = code[0]
        self.location = Location.Location(0, 1, self.line_number, self.file_name)
        self.error = None

    def advance(self):
        self.index += 1
        if self.index < len(self.code):
            self.character = self.code[self.index]
        else:
            self.character = None
        self.location = Location.Location(self.index, self.index + 1, self.line_number, self.file_name)

    def lex(self):
        tokens = []
        while self.character != None and self.error == None:
            if self.character in '+-*/()=#':
                match self.character:
                    case '+':
                        tokens.append(Token.Binary_Operator_Token('Plus', self.location))
                        self.advance()
                    case '-':
                        tokens.append(Token.Binary_Operator_Token('Minus', self.location))
                        self.advance()
                    case '*':
                        tokens.append(Token.Binary_Operator_Token('Multiply', self.location))
                        self.advance()
                    case '/':
                        tokens.append(Token.Binary_Operator_Token('Divide', self.location))
                        self.advance()
                    case '(':
                        tokens.append(Token.Binary_Operator_Token('Left Parenthesis', self.location))
                        self.advance()
                    case ')':
                        tokens.append(Token.Binary_Operator_Token('Right Parenthesis', self.location))
                        self.advance()
                    case '=':
                        tokens.append(Token.Binary_Operator_Token('Equals', self.location))
                        self.advance()
                    case '#':
                        tokens.append(self.lex_integer_or_float())
            elif self.character in ' \t':
                self.advance()
            elif self.character in constants.VALID_WORD_CHARACTERS:
                tokens.append(self.lex_keyword_or_indentifier())
            else:
                self.error = Error.Error('Illegal Character', self.character, self.location)
        tokens.append(Token.Token('End of File', self.location))
        return tokens, self.error
    
    def lex_integer_or_float(self):
        left_bound = self.index
        self.advance()
        number = ''
        if self.character == '-':
            number += '-'
            self.advance()
        while self.character != None and self.character in constants.DIGITS + '.' and self.error == None:
            if self.character == '.' and '.' in number:
                self.error = Error.Error('Illegal Character', '.', self.location)
            else:
                number += self.character
                self.advance()
        if len(number) == 0:
            self.error = Error.Error('Illegal Character', '#', Location.Location(left_bound, left_bound + 1, self.line_number, self.file_name))
        else:
            if '.' in number:
                return Token.Value_Token('Float', float(number), Location.Location(left_bound, self.index, self.line_number, self.file_name))
            else:
                return Token.Value_Token('Integer', int(number), Location.Location(left_bound, self.index, self.line_number, self.file_name))
            
    def lex_keyword_or_indentifier(self):
        left_bound = self.index
        word = ''
        while self.character != None and self.character in constants.VALID_WORD_CHARACTERS:
            word += self.character
            self.advance()
        if word in constants.KEYWORDS:
            name = 'Keyword'
        else:
            name = 'Indentifier'
        return Token.Value_Token(name, word, Location.Location(left_bound, self.index, self.line_number, self.file_name))
