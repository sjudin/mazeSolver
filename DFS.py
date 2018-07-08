import collections

def dfs(g):
    stack = list()
    visited = collections.OrderedDict()
    dist = 0

    stack.append(g.graph[str(0) + str(g.maze.entrance)])

    while stack:
        temp = stack.pop()
        visited[str(temp.x) + str(temp.y)] = temp

        if (str(temp.x) + str(temp.y)) == (str(g.endNode.x) + str(g.endNode.y)):
            #for v in visited:
            #    print(v)
            return visited

        for adjacent, weight in temp.linked:
            dist = dist + weight
            if adjacent not in visited.values():
                stack.append(adjacent)

    return None

