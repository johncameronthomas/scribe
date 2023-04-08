class Node:
    def __init__(self, value, location):
        self.value = value
        self.location = location

    def __repr__(self):
        return str(self.value)
    
class Integer_Node(Node):
    def __init__(self, value, location):
        super().__init__(value, location)

class Float_Node(Node):
    def __init__(self, value, location):
        super().__init__(value, location)
    
class Binary_Operation_Node(Node):
    def __init__(self, location, left_child, right_child):
        super().__init__(None, location)
        self.left_child = left_child
        self.right_child = right_child

class Subtraction_Node(Binary_Operation_Node):
    def __init__(self, location, left_child, right_child):
        super().__init__(location, left_child, right_child)
    
    def __repr__(self):
        return '({} - {})'.format(self.left_child, self.right_child)
    
class Addition_Node(Binary_Operation_Node):
    def __init__(self, location, left_child, right_child):
        super().__init__(location, left_child, right_child)
    
    def __repr__(self):
        return '({} + {})'.format(self.left_child, self.right_child)
    
class Division_Node(Binary_Operation_Node):
    def __init__(self, location, left_child, right_child):
        super().__init__(location, left_child, right_child)
    
    def __repr__(self):
        return '({} / {})'.format(self.left_child, self.right_child)
    
class Multiplication_Node(Binary_Operation_Node):
    def __init__(self, location, left_child, right_child):
        super().__init__(location, left_child, right_child)
    
    def __repr__(self):
        return '({} * {})'.format(self.left_child, self.right_child)