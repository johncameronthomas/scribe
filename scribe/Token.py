class Token:
    def __init__(self, value, location):
        self.value = value
        self.location = location
    
class Plus_Token(Token):
    def __init__(self, location):
        super().__init__(None, location)
    
    def __repr__(self):
        return '+'
    
class Minus_Token(Token):
    def __init__(self, location):
        super().__init__(None, location)
    
    def __repr__(self):
        return '-'
    
class Multiply_Token(Token):
    def __init__(self, location):
        super().__init__(None, location)
    
    def __repr__(self):
        return '*'
    
class Divide_Token(Token):
    def __init__(self, location):
        super().__init__(None, location)
    
    def __repr__(self):
        return '/'
    
class Left_Parenthesis_Token(Token):
    def __init__(self, location):
        super().__init__(None, location)
    
    def __repr__(self):
        return '('

class Right_Parenthesis_Token(Token):
    def __init__(self, location):
        super().__init__(None, location)
    
    def __repr__(self):
        return ')'
    
class Integer_Token(Token):
    def __init__(self, value, location):
        super().__init__(value, location)

    def __repr__(self):
        return str(self.value)
    
class Float_Token(Token):
    def __init__(self, value, location):
        super().__init__(value, location)

    def __repr__(self):
        return str(self.value)
    
class EOF_Token(Token):
    def __init__(self, location):
        super().__init__(None, location)

    def __repr__(self):
        return 'EOF'