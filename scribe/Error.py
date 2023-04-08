class Error:
    def __init__(self, message, location):
        self.message = message
        self.location = location
    
class Illegal_Character_Error(Error):
    def __init__(self, character, location):
        super().__init__(character, location)
    
    def __repr__(self):
        return "Illegal Character Error: '{}'".format(self.message)
    
class Invalid_Syntax_Error(Error):
    def __init__(self, details, location):
        super().__init__(details, location)

    def __repr__(self):
        return 'Invalid Syntax Error: {}'.format(self.message)
    
class Division_By_Zero_Error(Error):
    def __init__(self, location):
        super().__init__(None, location)

    def __repr__(self):
        return 'Division By Zero Error'