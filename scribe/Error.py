class Error:
    def __init__(self, name, details):
        self.name = name
        self.details = details

    def __repr__(self):
        return '{} Error: {}'.format(self.name, self.details)
    
class Illegal_Character(Error):
    def __init__(self, character):
        super().__init__('Illegal Character', "'{}'".format(character))