#Takes a image and returns a graph object for that image

from image import Maze
from node import Node


class Graph:
    """Graph contains list of neighbouring nodes paired with the weight of these"""
    def __init__(self,path):
        self.maze = Maze(path)
        self.graph = []
        self.node_place()
        print(self.graph)

    def node_place(self):
        """"Takes a maze_array and places nodes in relevant places"""
        previous_x = self.maze.array[0][0]
        previous_y = self.maze.array[0][0]

        for x in range(1, self.maze.width - 1):

            previous_x = x

            for y in range(1, self.maze.height - 1):
                if previous_y == 0:
                    self.graph.append((Node(x, y), 0))
                previous_y = y

g = Graph('images/tiny.png')
print('hello')