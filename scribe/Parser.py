import Token
import Node
import Error

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.token = tokens[0]
        self.error = None

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.token = self.tokens[self.index]
    
    def create_subtraction_node(self):
        return self.create_binary_operation_node(self.create_addition_node, Token.Minus_Token, Node.Subtraction_Node)

    def create_addition_node(self):
        return self.create_binary_operation_node(self.create_division_node, Token.Plus_Token, Node.Addition_Node)

    def create_division_node(self):
        return self.create_binary_operation_node(self.create_multiplication_node, Token.Divide_Token, Node.Division_Node)
    
    def create_multiplication_node(self):
        return self.create_binary_operation_node(self.create_number_node, Token.Multiply_Token, Node.Multiplication_Node)

    def create_number_node(self):
        match type(self.token):
            case Token.Integer_Token:
                token = self.token
                self.advance()
                return Node.Integer_Node(token.value, token.location)
            case Token.Float_Token:
                token = self.token
                self.advance()
                return Node.Float_Node(token.value, token.location)
            case Token.Left_Parenthesis_Token:
                self.advance()
                node = self.create_subtraction_node()
                if self.error:
                    return node
                else:
                    if type(self.token) == Token.Right_Parenthesis_Token:
                        self.advance()
                        return node
                    else:
                        self.error = Error.Invalid_Syntax_Error("Expected ')'", self.token.location)
                        return node
            case _:
                self.error = Error.Invalid_Syntax_Error('Expeced Integer or Float.', self.token.location)

    def create_binary_operation_node(self, function, valid_token_type, node_type):
        left_child = function()
        while type(self.token) == valid_token_type:
            token = self.token
            self.advance()
            right_child = function()
            left_child = node_type(token.location, left_child, right_child)
        return left_child

    def parse(self):
        node = self.create_subtraction_node()
        if not self.error and type(self.token) != Token.EOF_Token:
            self.error = Error.Invalid_Syntax_Error('Expected Operator.', self.token.location)
        return node, self.error