class Node:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)
    
class Integer_Node(Node):
    def __init__(self, value):
        super().__init__(value)

class Float_Node(Node):
    def __init__(self, value):
        super().__init__(value)
    
class Binary_Operation_Node(Node):
    def __init__(self, value, left_child, right_child):
        super().__init__(value)
        self.left_child = left_child
        self.right_child = right_child

class Subtraction_Node(Binary_Operation_Node):
    def __init__(self, left_child, right_child):
        super().__init__(None, left_child, right_child)
    
    def __repr__(self):
        return '({} - {})'.format(self.left_child, self.right_child)
    
class Addition_Node(Binary_Operation_Node):
    def __init__(self, left_child, right_child):
        super().__init__(None, left_child, right_child)
    
    def __repr__(self):
        return '({} + {})'.format(self.left_child, self.right_child)
    
class Division_Node(Binary_Operation_Node):
    def __init__(self, left_child, right_child):
        super().__init__(None, left_child, right_child)
    
    def __repr__(self):
        return '({} / {})'.format(self.left_child, self.right_child)
    
class Multiplication_Node(Binary_Operation_Node):
    def __init__(self, left_child, right_child):
        super().__init__(None, left_child, right_child)
    
    def __repr__(self):
        return '({} * {})'.format(self.left_child, self.right_child)