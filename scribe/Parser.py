import Error
import Node

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

    def create_binary_operation_node(self, next_node_creation_function, valid_token_name):
        left_child = next_node_creation_function()
        while self.token.name == valid_token_name and self.error == None:
            token = self.token
            self.advance()
            right_child = next_node_creation_function()
            left_child = token.convert_to_node(left_child, right_child)
        return left_child
    
    def create_variable_assignment_node(self):
        if self.token.name == 'Keyword':
            data_type = self.token.convert_to_node()
            self.advance()
            if self.token.name != 'Indentifier':
                self.error = Error.Error('Invalid Syntax', 'Expected Indentifier.', self.token.location)
            else:
                name = self.token.convert_to_node()
                self.advance()
                if self.token.name != 'Equals':
                    self.error = Error.Error('Invalid Syntax', "Expected '='.", self.token.location)
                else:
                    location = self.token.location
                    self.advance()
                    value = self.create_subtraction_node()
                    return Node.Ternary_Operation_Node('Variable Assignment', data_type, name, value, location)
        return self.create_subtraction_node()
    
    def create_subtraction_node(self):
        return self.create_binary_operation_node(self.create_addition_node, 'Minus')
    
    def create_addition_node(self):
        return self.create_binary_operation_node(self.create_division_node, 'Plus')
    
    def create_division_node(self):
        return self.create_binary_operation_node(self.create_multiplication_node, 'Divide')
    
    def create_multiplication_node(self):
        return self.create_binary_operation_node(self.create_contained_node, 'Multiply')

    def create_contained_node(self):
        if self.token.name == 'Left Parenthesis':
            self.advance()
            node = self.create_variable_assignment_node()
            if not self.error:
                if self.token.name == 'Right Parenthesis':
                    self.advance()
                    return node
                else:
                    self.error = Error.Error('Invalid Syntax', "Expected ')'", self.token.location)
        else:
            return self.create_number_node()
    
    def create_number_node(self):
        if self.token.name in ('Integer', 'Float', 'Indentifier'):
            token = self.token
            self.advance()
            return token.convert_to_node()
        else:
            self.error = Error.Error('Invalid Syntax', "Expected '#'", self.token.location)

    def parse(self):
        node = self.create_variable_assignment_node()
        if not self.error and self.token.name != 'End of File':
            print(self.token)
            self.error = Error.Error('Invalid Syntax', "Expected '+', '-', '*', or '/'.", self.token.location)
        return node, self.error