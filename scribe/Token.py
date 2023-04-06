class Token:
    def __init__(self, value):
        self.value = value
    
class Plus_Token(Token):
    def __init__(self):
        super().__init__(None)
    
    def __repr__(self):
        return '+'
    
class Minus_Token(Token):
    def __init__(self):
        super().__init__(None)
    
    def __repr__(self):
        return '-'
    
class Multiply_Token(Token):
    def __init__(self):
        super().__init__(None)
    
    def __repr__(self):
        return '*'
    
class Divide_Token(Token):
    def __init__(self):
        super().__init__(None)
    
    def __repr__(self):
        return '/'
    
class Left_Parenthesis_Token(Token):
    def __init__(self):
        super().__init__(None)
    
    def __repr__(self):
        return '('

class Right_Parenthesis_Token(Token):
    def __init__(self):
        super().__init__(None)
    
    def __repr__(self):
        return ')'
    
class Integer_Token(Token):
    def __init__(self, value):
        super().__init__(value)

    def __repr__(self):
        return str(self.value)
    
class Float_Token(Token):
    def __init__(self, value):
        super().__init__(value)

    def __repr__(self):
        return str(self.value)
    
class EOF_Token(Token):
    def __init__(self):
        super().__init__(None)

    def __repr__(self):
        return 'EOF'