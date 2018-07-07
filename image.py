from PIL import Image
from node import Node
from pandas import DataFrame

class Maze:
    def __init__(self,path):
        self.maze_image = Image.open(path)
        self.height = self.maze_image.height
        self.width = self.maze_image.width

        self.array = [[0 for x in range(self.width)] for y in range(self.height)]
        self.populate_array()

        self.entrance = self.find_passways(self.array[0])
        self.exit = self.find_passways(self.array[-1])


    def populate_array(self):
        for x in range(self.maze_image.width):
            for y in range(self.maze_image.height):
                self.array[x][y] = Image.Image.getpixel(self.maze_image, (y, x))

    def find_passways(self,row):
        for counter in enumerate(row):
            if counter[1] == 1:
                return counter[0]


# maze = Maze('images/tiny.png')
# print(DataFrame(maze.array))
# print (maze.array[0])
# test1 = Node(1, 1)
# test2 = Node(1, 2)
# test1.connect(test2)


