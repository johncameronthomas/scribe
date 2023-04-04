class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __repr__(self):
        if self.value:
            return '{} Token: {}'.format(self.name, self.value)
        else:
            return '{} Token'.format(self.name)

class Plus(Token):
    def __init__(self):
        super().__init__('Plus', None)

class Minus(Token):
    def __init__(self):
        super().__init__('Minus', None)

class Multiply(Token):
    def __init__(self):
        super().__init__('Multiply', None)

class Divide(Token):
    def __init__(self):
        super().__init__('Divide', None)

class Left_Parenthesis(Token):
    def __init__(self):
        super().__init__('Left Parenthesis', None)

class Right_Parenthesis(Token):
    def __init__(self):
        super().__init__('Right Parenthesis', None)

class Integer(Token):
    def __init__(self, value):
        super().__init__('Integer', value)

class Float(Token):
    def __init__(self, value):
        super().__init__('Float', value)