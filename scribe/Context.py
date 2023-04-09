class Context:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.symbol_table = {}

    def __repr__(self):
        if self.parent == None:
            return self.name
        else:
            return '{} -> {}'.format(self.parent, self.name)
    
    def get(self, name):
        value = self.symbol_table.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        else:
            return value
        
    def set(self, name, value):
        self.symbol_table.update({name: value})
        return value