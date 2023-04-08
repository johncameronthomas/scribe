class Error:
    def __init__(self, message, location):
        self.message = message
        self.location = location
    
class Illegal_Character_Error(Error):
    def __init__(self, character, location):
        super().__init__(character, location)
    
class Invalid_Syntax_Error(Error):
    def __init__(self, message, location):
        super().__init__(message, location)

class Division_By_Zero_Error(Error):
    def __init__(self, location):
        super().__init__(None, location)