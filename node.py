
class Node:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.linked = []

    def connect(self, node, weight):
        if type(weight) is not int:
            raise ValueError

        self.linked.append((node, weight))

    def __str__(self):
        connected = []
        for node in self.linked:
            connected.append((node[0].x, node[0].y, node[1]))

        return str('%s,%s Linked nodes: %s' % (self.x, self.y, connected))
