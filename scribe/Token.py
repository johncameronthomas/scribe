import Node

class Token:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return '{} Token'.format(self.name)

    def convert_to_node(self):
        return Node.Node(self.name, self.location)

class Value_Token(Token):
    def __init__(self, name, value, location):
        super().__init__(name, location)
        self.value = value
    
    def __repr__(self):
        return '{} Token: {}'.format(self.name, self.value)

    def convert_to_node(self):
        return Node.Value_Node(self.name, self.value, self.location)
    
class Binary_Operator_Token(Token):
    def convert_to_node(self, left_child, right_child):
        match self.name:
            case 'Plus':
                name = 'Addition'
            case 'Minus':
                name = 'Subtraction'
            case 'Multiply':
                name = 'Multiplication'
            case 'Divide':
                name = 'Division'
            case _:
                name = None
        return Node.Binary_Operation_Node(name, left_child, right_child, self.location)