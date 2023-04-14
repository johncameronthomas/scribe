from Error import Runtime_Error

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
    
    def define_symbol(self, identifier: str) -> bool:
        if identifier in self.symbol_table.keys():
            raise ValueError()
        else:
            self.symbol_table[identifier] = None

    def delete_symbol(self, identifier: str) -> bool:
        if identifier in self.symbol_table:
            del self.symbol_table[identifier]
        else:
            raise ValueError()

    def get_symbol(self, identifier: str):
        if identifier not in self.symbol_table:
            if self.parent != None:
                return self.parent.get_symbol(identifier)
            else:
                raise ValueError()
        else:
            return self.symbol_table[identifier]

    def set_symbol(self, identifier: str, data):
        if identifier not in self.symbol_table:
            if self.parent != None:
                return self.parent.set_symbol(identifier, data)
            else:
                raise ValueError()
        else:
            self.symbol_table[identifier] = data