from typing import Union, Tuple, Type

from Token import *
from Error import Error
from Location import Location
from constants import VALID_WORD_CHARACTERS, VALID_NUMBER_CHARACTERS

class Lexer:
    def __init__(self, code: str, line_number: int, file_name: str) -> None:
        self.code = code
        self.line_number = line_number
        self.file_name = file_name

        self.index = 0
        self.character = code[0]
        self.error = None

    def advance(self) -> None:
        self.index += 1
        if self.index < len(self.code):
            self.character = self.code[self.index]
        else:
            self.character = None

    def lex(self) -> Tuple[Tuple[*Type[Token]], Error]:
        tokens = []
        while self.character != None and self.error == None:
            if self.character == '+':
                tokens.append(Token('Plus', self.create_location_with_length(1)))
                self.advance()
            elif self.character == '-':
                tokens.append(Token('Minus', self.create_location_with_length(1)))
                self.advance()
            elif self.character == '*':
                tokens.append(Token('Multiply', self.create_location_with_length(1)))
                self.advance()
            elif self.character == '/':
                tokens.append(Token('Divide', self.create_location_with_length(1)))
                self.advance()
            elif self.character == '(':
                tokens.append(Token('Left Parenthesis', self.create_location_with_length(1)))
                self.advance()
            elif self.character == ')':
                tokens.append(Token('Right Parenthesis', self.create_location_with_length(1)))
                self.advance()
            elif self.character == '=':
                tokens.append(Token('Equals', self.create_location_with_length(1)))
                self.advance()
            elif self.character == '#':
                tokens.append(self.lex_number())
            elif self.character in VALID_WORD_CHARACTERS:
                tokens.append(self.lex_word())
            elif self.character in ' \t':
                self.advance()
            else:
                self.error = Error('Illegal Character', self.character, self.create_location_with_length(1))
        tokens.append(Token('End Of Line', self.create_location_with_length(1)))
        tokens = tuple(tokens)
        return tokens, self.error

    def lex_number(self) -> Data_Token:
        left_bound = self.index
        self.advance()
        number = ''
        if self.character == '-':
            number += '-'
            self.advance()
        while self.character != None and self.character in VALID_NUMBER_CHARACTERS and self.error == None:
            if self.character == '.' and '.' in number:
                self.error = Error('Illegal Character', '.', self.location)
            else:
                number += self.character
                self.advance()
        if len(number) == 0:
            self.error = Error('Illegal Character', '#', Location(left_bound, left_bound + 1, self.line_number, self.file_name))
        else:
            location = self.create_location_with_bounds(left_bound, self.index)
            if '.' in number:
                return Data_Token('Rational', float(number), location)
            else:
                return Data_Token('Integer', int(number), location)

    def lex_word(self) -> Union[Token, Data_Token]:
        left_bound = self.index
        word = ''
        while self.character != None and self.character in VALID_WORD_CHARACTERS:
            word += self.character
            self.advance()
        location = self.create_location_with_bounds(left_bound, self.index)
        if word == 'define':
            return Token('Define', location)
        else:
            return Data_Token('Identifier', word, location)

    def create_location_with_bounds(self, left_bound: int, right_bound: int) -> Location:
        return Location(left_bound, right_bound, self.line_number, self.file_name)

    def create_location_with_length(self, length: int) -> Location:
        return Location(self.index, self.index + length, self.line_number, self.file_name)