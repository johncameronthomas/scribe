from Location import Location

class Node:
    def __init__(self, name: str, location: Location) -> None:
        self.name = name
        self.location = location

    def __repr__(self) -> str:
        return '({} Node)'.format(self.name)

class Data_Node(Node):
    def __init__(self, name: str, data, location: Location) -> None:
        super().__init__(name, location)
        self.data = data

    def __repr__(self) -> str:
        return '({} Node: {})'.format(self.name, self.data)

class Unary_Operation_Node(Node):
    def __init__(self, name: str, child, location: Location) -> None:
        super().__init__(name, location)
        self.child = child

    def __repr__(self) -> str:
        return '({} Node <- {})'.format(self.name, self.child)

class Binary_Operation_Node(Node):
    def __init__(self, name: str, left_child, right_child, location: Location) -> None:
        super().__init__(name, location)
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self) -> str:
        return '({} -> {} Node <- {})'.format(self.left_child, self.name, self.right_child)

class Ternary_Operation_Node(Binary_Operation_Node):
    def __init__(self, name: str, left_child, middle_child, right_child, location: Location) -> None:
        super().__init__(name, left_child, right_child, location)
        self.middle_child = middle_child

    def __repr__(self) -> str:
        return '({} Node <- {} {} {})'.format(self.name, self.left_child, self.middle_child, self.right_child)