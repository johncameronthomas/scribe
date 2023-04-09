class Node:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Value_Node(Node):
    def __init__(self, name, value, location):
        super().__init__(name, location)
        self.value = value

    def __repr__(self):
        return str(self.value)

class Binary_Operation_Node(Node):
    def __init__(self, name, location, left_child, right_child):
        super().__init__(name, location)
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return '({} {} {})'.format(self.left_child, self.name, self.right_child)