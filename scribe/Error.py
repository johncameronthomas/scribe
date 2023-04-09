class Error:
    def __init__(self, name, message, location):
        self.name = name
        self.message = message
        self.location = location

    def __repr__(self):
        return '{} Error: {}'.format(self.name, self.message)
    
    def print_error(self, code):
        length = self.location.right_bound - self.location.left_bound
        arrow_string = (' ' * self.location.left_bound) + ('^' * length)
        print("Line {} in file '{}'.".format(self.location.line_number, self.location.file_name))
        print(code)
        print(arrow_string)
        print('{}: {}'.format(self.name, self.message))

    
class Runtime_Error(Error):
    def __init__(self, name, message, location, context):
        super().__init__(name, message, location)
        self.context = context

    def print_error(self, code):
        print('Traceback:')
        print(self.context)
        super().print_error(code)