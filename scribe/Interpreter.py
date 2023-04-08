import Token
import Node

class Interpreter:
    def interpret(self, node):
        match type(node.token):
            case Token.Minus_Token:
                pass
            case Token.Plus_Token:
                pass