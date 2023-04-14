from Error import Runtime_Error
from Context import Context
from Node import Data_Node

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
                return node.data
            case 'Rational':
                return node.data
            case 'Symbol Assignment':
                try:
                    return self.context.set_symbol(self.evaluate_node(node.left_child).data, self.evaluate_node(node.right_child))
                except:
                    self.error = Runtime_Error('Symbol Not Defined', node.left_child, node.location, self.context)
            case 'Symbol Definition':
                try:
                    self.context.define_symbol(node.child.data)
                    return Data_Node('Identifier', node.child.data, node.location)
                except:
                    self.error = Runtime_Error('Symbol Already Defined', node.child.data, node.location, self.context)
            case 'Identifier':
                try:
                    result = self.context.get_symbol(node.data)
                except:
                    self.error = Runtime_Error('Undefined Variable', node.data, node.location, self.context)
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
                    self.error = Runtime_Error('Division by Zero', '', node.location, self.context)
                    return 0
            case 'Multiplication':
                return self.evaluate_node(node.left_child) * self.evaluate_node(node.right_child)