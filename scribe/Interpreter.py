import Error

class Interpreter:
    def __init__(self, node):
        self.node = node
        self.error = None

    def interpret(self):
        return self.evaluate_node(self.node), self.error

    def evaluate_node(self, node):
        match node.name:
            case 'Integer':
                return node.value
            case 'Float':
                return node.value
            case 'Subtraction':
                return self.evaluate_node(node.left_child) - self.evaluate_node(node.right_child)
            case 'Addition':
                return self.evaluate_node(node.left_child) + self.evaluate_node(node.right_child)
            case 'Division':
                try:
                    return self.evaluate_node(node.left_child) / self.evaluate_node(node.right_child)
                except:
                    self.error = Error.Runtime_Error('Division by Zero', '', node.location, None)
                    return 0
            case 'Multiplication':
                return self.evaluate_node(node.left_child) * self.evaluate_node(node.right_child)