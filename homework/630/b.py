from collections import deque


infinity = float("inf")

def bfs(G, source, sink, parent):
    visited = set()

    queue = deque()
    queue.append(source)

    visited.add(source)
 
    while queue:
        node = queue.popleft()

        for i in range(len(G[node])):
            if i not in visited and G[node][i] > 0:
                queue.append(i)
                visited.add(i)
                parent[i] = node
 
    return sink in visited


def ford_fulkerson(G, source, sink):
    parent = [-1] * (len(G))
    max_flow = 0

    while bfs(G, source, sink, parent):
        path_flow = infinity
        s = sink
 
        while s != source:
            path_flow = min(path_flow, G[parent[s]][s])
            s = parent[s]
 
        max_flow += path_flow
        v = sink
 
        while v != source:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]

    return max_flow


def main():
    #G = make_graph()
    n, m = map(int, input().split())
    source = 0
    sink = n - 1
    graph = [[0 for _ in range(n)] for _ in range(n)]
    #print(graph)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a-1][b-1] += c
        #graph[b-1][a-1] = c
    #print(graph)
    #print graph
    
    max_flow = ford_fulkerson(graph, source, sink)
    print(f'{max_flow}')


main()