class Location:
    def __init__(self, left_bound, right_bound, line_number, file_name):
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.line_number = line_number
        self.file_name = file_name