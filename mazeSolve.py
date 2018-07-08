from graphCreator import Graph
from DFS import dfs
import time

path = "images/perfect2k.png"


class MazeSolver:

    def __init__(self, path):
        start = time.time()
        print('Setting up graph')
        g = Graph(path)
        print('Graph set up in %s seconds' % (time.time() - start))

        algo_list = ['[1]DFS']
        algo_keys = [1]
        #print(g)
        #input_var = input("Which algorithm would you like to test? The available ones are: " + str(algo_list))

        #if int(input_var) not in algo_keys:
        #    print('Wrong input, try again!')
        #elif int(input_var) is 1:
        #    print('DFS!')
        start = time.time()
        print('beginning DFS...')
        solved = dfs(g)
        print('DFS finished in %s seconds' % (time.time() - start))

        if solved:
            pass
            #g.maze.paint_solved_path(solved)
            #g.maze.save_solved(path)
        else:
            print('No solution found!')
            g.maze.save_solved(path)



m = MazeSolver(path)

