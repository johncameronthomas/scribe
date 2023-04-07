class Error:
    def __init__(self, details):
        self.details = details
    
class Illegal_Character_Error(Error):
    def __init__(self, character):
        super().__init__(character)
    
    def __repr__(self):
        return "Illegal Character Error: '{}'".format(self.details)
    
class Invalid_Syntax_Error(Error):
    def __init__(self, details):
        super().__init__(details)

    def __repr__(self):
        return 'Invalid Syntax Error: {}'.format(self.details)