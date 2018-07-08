from PIL import Image
from node import Node

class Maze:
    def __init__(self, path):
        self.maze_image = Image.open(path)
        self.width, self.height = self.maze_image.size

        self.array = [[0 for x in range(self.height)] for y in range(self.width)]
        self.__populate_array()

        self.entrance = self.__find_passways(self.array[0])
        self.exit = self.__find_passways(self.array[-1])

        self.maze_image = self.maze_image.convert('RGB')
        self.__impixels = self.maze_image.load()

        print('Array populated!')

    def __populate_array(self):
        for row in range(self.maze_image.height):
            for column in range(self.maze_image.width):
                self.array[row][column] = Image.Image.getpixel(self.maze_image, (column, row))

    @staticmethod
    def __find_passways(row: list) -> int:
        for counter in enumerate(row):
            if counter[1] == 1:
                return counter[0]

    def paint_solved(self, x, y, color):
        if x > self.height or y > self.width:
            raise IndexError

        if x or y is 0:
            print('bug!')

        self.__impixels[y, x] = color

    def paint_path(self, point_1, point_2):
        vertical = point_1.x - point_2.x
        horizontal = point_1.y - point_2.y

        if vertical is 0:
            """Paint horizontal"""
            for a in range(min(point_1.y, point_2.y), max(point_1.y, point_2.y)):
                self.paint_solved(point_1.x, a, (0, 255, 0))

        elif horizontal is 0:
            """Paint vertical"""
            for a in range(min(point_1.x, point_2.x), max(point_1.x, point_2.x)):
                self.paint_solved(point_1.y, a, (0, 255, 0))

    def paint_solved_path(self, path):
        previous = next(iter(path.values()))
        for n in path.values():
            self.paint_path(n, previous)
            previous = n

    def save_solved(self, path):
        solved_path = path.split('.')
        solved_path = solved_path[0] + '_solved.png'
        self.maze_image.save(solved_path)

#test = Maze("images/tiny.png")
#test.paint_solved(0,5,(255,0,0))
#test.save_solved("images/tiny.png")