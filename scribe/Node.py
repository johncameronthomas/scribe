class Node:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return '{}'.format(self.token)
    
class Binary_Operation_Node(Node):
    def __init__(self, token, left_child, right_child):
        super().__init__(token)
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return '({} {} {})'.format(self.left_child, self.token, self.right_child)
    
class Unary_Operation_Node(Node):
    def __init__(self, token, child):
        super().__init__(token)
        self.child = child

    def __repr__(self):
        return '({}{})'.format(self.token, self.child)