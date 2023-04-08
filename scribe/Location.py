class Location:
    def __init__(self, index_of_first_character, index_of_last_character, line, context):
        self.index_of_first_character = index_of_first_character
        self.index_of_last_character = index_of_last_character
        self.line = line
        self.context = context