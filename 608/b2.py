from collections import defaultdict

def dfs(src, dest, graph, path, allPaths):
    # Add the current vertex to the path
    path.append(src)

    # Store the path when destination is reached
    if src == dest:
        allPaths.append(path.copy())
    else:
        for adj_node in graph[src]:
            dfs(adj_node, dest, graph, path, allPaths)

    # remove the current vertex from the path
    path.pop()

def findPaths(v, edges, src, dest):
    graph = [[] for _ in range(v)]

    # Build the graph from edges
    for edge in edges:
        graph[edge[0]].append(edge[1])

    allPaths = []
    path = []

    dfs(src, dest, graph, path, allPaths)

    return allPaths

n, m = map(int, input().split())

edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append([a, b])
    

#edges = [[0, 3], [0, 1], [1, 3], [2, 0], [2, 1]]
src = 1
dest = n
v = n

paths = findPaths(v, edges, src, dest)
print('_______________')
print(len(paths))
for path in paths:
    print(len(path))
    for vtx in path:
        print(vtx, end=" ")
    print()