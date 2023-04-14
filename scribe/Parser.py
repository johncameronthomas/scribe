from typing import Tuple, Type

from Error import Error
from Node import *
from Token import *

class Parser:
    def __init__(self, tokens: Tuple[*Type[Token]]) -> None:
        self.tokens = tokens

        self.index = 0
        self.token = tokens[0]
        self.order_of_creation_functions = []
        self.error = None

    def advance(self) -> None:
        self.index += 1
        if self.index < len(self.tokens):
            self.token = self.tokens[self.index]

    def create_symbol_assignment_node(self):
        left_child = self.create_symbol_definition_node()
        while self.token.name == 'Equals' and self.error == None:
            token = self.token
            self.advance()
            right_child = self.create_symbol_definition_node()
            left_child = Binary_Operation_Node('Symbol Assignment Node', left_child, right_child, token.location)
        return left_child

    def create_symbol_definition_node(self):
        if self.token.name == 'Define':
            location = self.token.location
            self.advance()
            if self.token.name == 'Identifier':
                identifier = self.token.convert_to_node()
                self.advance()
                return Unary_Operation_Node('Symbol Definition', identifier, location)
            else:
                self.error = Error('Invalid Syntax', 'Expected Identifier.', self.token.location)
        else:
            return self.create_subtraction_node()

    def create_subtraction_node(self):
        left_child = self.create_addition_node()
        while self.token.name == 'Minus' and self.error == None:
            token = self.token
            self.advance()
            right_child = self.create_addition_node()
            left_child = Binary_Operation_Node('Subtraction', left_child, right_child, token.location)
        return left_child

    def create_addition_node(self):
        left_child = self.create_division_node()
        while self.token.name == 'Plus' and self.error == None:
            token = self.token
            self.advance()
            right_child = self.create_division_node()
            left_child = Binary_Operation_Node('Addition', left_child, right_child, token.location)
        return left_child
    
    def create_division_node(self):
        left_child = self.create_multiplication_node()
        while self.token.name == 'Divide' and self.error == None:
            token = self.token
            self.advance()
            right_child = self.create_multiplication_node()
            left_child = Binary_Operation_Node('Division', left_child, right_child, token.location)
        return left_child

    def create_multiplication_node(self):
        left_child = self.create_parentheses_node()
        while self.token.name == 'Multiply' and self.error == None:
            token = self.token
            self.advance()
            right_child = self.create_parentheses_node()
            left_child = Binary_Operation_Node('Multiplication', left_child, right_child, token.location)
        return left_child
    
    def create_parentheses_node(self):
        if self.token.name == 'Left Parenthesis':
            self.advance()
            node = self.create_symbol_assignment_node()
            if not self.error:
                if self.token.name == 'Right Parenthesis':
                    self.advance()
                    return node
                else:
                    self.error = Error('Invalid Syntax', "Expected ')'", self.token.location)
        else:
            return self.create_data_node()

    def create_data_node(self):
        if self.token.name in ('Integer', 'Rational', 'Identifier'):
            token = self.token
            self.advance()
            return token.convert_to_node()
        else:
            self.error = Error('Invalid Syntax', "Expected '#' or Identifier.", self.token.location)

    def parse(self) -> tuple:
        node = self.create_symbol_assignment_node()
        if not self.error and self.token.name != 'End Of Line':
            self.error = Error('Invalid Syntax', "Expected '+', '-', '*', or '/'.", self.token.location)
        return node, self.error