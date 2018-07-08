#Takes a image and returns a graph object for that image

from image import Maze
from node import Node

class Graph:
    """Graph contains list of neighbouring nodes paired with the weight of these"""

    def __init__(self, path):
        self.maze = Maze(path)
        self.graph = dict()
        self.__node_place()

        self.startNode = Node(0, self.maze.entrance)
        self.endNode = Node(self.maze.height - 1, self.maze.exit)

        self.graph[str(0) + str(self.maze.entrance)] = Node(0, self.maze.entrance)
        self.graph[str(self.maze.height - 1) + str(self.maze.exit)] = Node(self.maze.height - 1, self.maze.exit)

        self.maze.paint_solved(self.startNode.x, self.startNode.y, (0, 0, 255))
        self.maze.paint_solved(self.endNode.x, self.endNode.y, (0, 0, 255))

        self.__link_nodes()

    def __node_place(self):
        """"Takes a maze_array and places nodes in relevant places"""

        for row in range(1, self.maze.height - 1):
            for column in range(1, self.maze.width - 1):
                if self.__rule_check(row, column):
                    self.graph[str(row) + str(column)] = (Node(row, column))
                    self.maze.paint_solved(column, row, (0, 255, 0))


    def __link_nodes(self):
        """Take each node in graph, walk north, west, south and east until wall or node is encountered. Connect nodes if node is found"""
        def __link_north(node):
            if node.x is 0:
                return

            pos = (node.x - 1, node.y)
            step = 0

            while self.maze.array[pos[0]][pos[1]] is not 0:
                step = step + 1

                if str(pos[0]) + str(pos[1]) in self.graph:
                    node.connect(self.graph[str(pos[0]) + str(pos[1])], step)
                    break
                pos = (pos[0] - 1, pos[1])

        def __link_south(node):
            if node.x is self.maze.height - 1:
                return

            try:
                pos = (node.x + 1, node.y)
                step = 0

                while self.maze.array[pos[0]][pos[1]] is not 0:
                    step = step + 1

                    if str(pos[0]) + str(pos[1]) in self.graph:
                        node.connect(self.graph[str(pos[0]) + str(pos[1])], step)
                        break
                    pos = (pos[0] + 1, pos[1])
            except IndexError:
                return

        def __link_east(node):
            pos = (node.x, node.y + 1)
            step = 0

            while self.maze.array[pos[0]][pos[1]] is not 0:
                step = step + 1

                if str(pos[0]) + str(pos[1]) in self.graph:
                    node.connect(self.graph[str(pos[0]) + str(pos[1])], step)
                    break
                pos = (pos[0], pos[1] + 1)

        def __link_west(node):
            pos = (node.x, node.y - 1)
            step = 0

            while self.maze.array[pos[0]][pos[1]] is not 0:
                step = step + 1

                if str(pos[0]) + str(pos[1]) in self.graph:
                    node.connect(self.graph[str(pos[0]) + str(pos[1])], step)
                    break
                pos = (pos[0], pos[1] - 1)

        for node in self.graph.values():
            __link_south(node)
            __link_north(node)
            __link_east(node)
            __link_west(node)


    def __rule_check(self, row, col):
        if self.maze.array[row][col] is 1 and self.maze.array[row][col - 1] is 0 and (self.maze.array[row - 1][col] is 0 or self.maze.array[row + 1][col] is 0):
            return True

        elif self.maze.array[row][col] is 1 and self.maze.array[row][col + 1] is 0 and (self.maze.array[row - 1][col] is 0 or self.maze.array[row + 1][col] is 0):
            return True

        elif self.maze.array[row][col] and self.maze.array[row][col - 1] and self.maze.array[row][col + 1] is 1 and (self.maze.array[row + 1][col] or self.maze.array[row - 1][col] is 1):
            return True

        elif self.maze.array[row][col] is 1 and self.maze.array[row + 1][col] is 1 and self.maze.array[row - 1][col] is 1 and (self.maze.array[row][col + 1] or self.maze.array[row][col - 1] is 1):
            return True

        return False

    def is_linked(self, node_1, node_2):
        return node_2 in self.graph[node_1]

    def get_node(self, row, col):
        return self.graph[str(row) + str(col)]

    def __str__(self):
        return_list = []

        for node in self.graph.values():
            return_list.append(str(node))

        return str(return_list)
