import Error

class Interpreter:
    def __init__(self, node, context):
        self.node = node
        self.context = context
        self.error = None

    def interpret(self):
        return self.evaluate_node(self.node), self.error

    def evaluate_node(self, node):
        match node.name:
            case 'Integer':
                return node.value
            case 'Float':
                return node.value
            case 'Variable Assignment':
                return self.context.set(node.middle_child.value, self.evaluate_node(node.right_child))
            case 'Indentifier':
                result = self.context.get(node.value)
                if result == None:
                    self.error = Error.Runtime_Error('Undefined Variable', "'{}' is undefined.".format(node.value), node.location, self.context)
                    return 0
                else:
                    return result
            case 'Subtraction':
                return self.evaluate_node(node.left_child) - self.evaluate_node(node.right_child)
            case 'Addition':
                return self.evaluate_node(node.left_child) + self.evaluate_node(node.right_child)
            case 'Division':
                try:
                    return self.evaluate_node(node.left_child) / self.evaluate_node(node.right_child)
                except:
                    self.error = Error.Runtime_Error('Division by Zero', '', node.location, self.context)
                    return 0
            case 'Multiplication':
                return self.evaluate_node(node.left_child) * self.evaluate_node(node.right_child)