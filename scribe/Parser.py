import Token
import Node

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.token = tokens[0]

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.token = self.tokens[self.index]
    
    def create_subtraction_node(self):
        return self.create_binary_operation_node(self.create_addition_node, Token.Minus_Token)

    def create_addition_node(self):
        return self.create_binary_operation_node(self.create_division_node, Token.Plus_Token)

    def create_division_node(self):
        return self.create_binary_operation_node(self.create_multiplication_node, Token.Divide_Token)
    
    def create_multiplication_node(self):
        return self.create_binary_operation_node(self.create_number_node, Token.Multiply_Token)

    def create_number_node(self):
        if type(self.token) in (Token.Integer_Token, Token.Float_Token):
            token = self.token
            self.advance()
            return Node.Node(token)

    def create_binary_operation_node(self, function, valid_token_type):
        left_child = function()
        while type(self.token) == valid_token_type:
            token = self.token
            self.advance()
            right_child = function()
            left_child = Node.Binary_Operation_Node(token, left_child, right_child)
        return left_child

    def parse(self):
        return self.create_subtraction_node()