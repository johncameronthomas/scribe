from Location import Location
from Node import Data_Node

class Token:
    def __init__(self, name: str, location: Location) -> None:
        self.name = name
        self.location = location

    def __repr__(self) -> str:
        return '{} Token'.format(self.name)

class Data_Token(Token):
    def __init__(self, name: str, data, location: Location) -> None:
        super().__init__(name, location)
        self.data = data

    def convert_to_node(self) -> Data_Node:
        return Data_Node(self.name, self.data, self.location)

    def __repr__(self) -> str:
        return '{} Token: {}'.format(self.name, self.data)