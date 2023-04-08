import Node
import Error

class Interpreter:
    def __init__(self, node):
        self.node = node
        self.error = None

    def interpret(self):
        return self.evaluate_node(self.node), self.error

    def evaluate_node(self, node):
        match type(node):
            case Node.Integer_Node:
                return node.value
            case Node.Float_Node:
                return node.value
            case Node.Subtraction_Node:
                return self.evaluate_node(node.left_child) - self.evaluate_node(node.right_child)
            case Node.Addition_Node:
                return self.evaluate_node(node.left_child) + self.evaluate_node(node.right_child)
            case Node.Division_Node:
                try:
                    return self.evaluate_node(node.left_child) / self.evaluate_node(node.right_child)
                except:
                    self.error = Error.Division_By_Zero_Error()
                    return 0
            case Node.Multiplication_Node:
                return self.evaluate_node(node.left_child) * self.evaluate_node(node.right_child)
            
    def create_integer_node_or_float_node(number):
        if type(number) == int:
            return Node.Integer_Node(number)
        elif type(number) == float:
            return Node.Float_Node(number)