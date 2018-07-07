
class Node:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.north = None
        self.west = None
        self.east = None
        self.south = None

        self.linked = list()

    def connect(self, node):
        self.linked.append(node)
        node.linked.append(self)
