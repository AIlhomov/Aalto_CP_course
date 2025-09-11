n, m = map(int, input().split())

#Uolevi pc is: 1
#Maija pc is: n

adjList = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())

    adjList[a].append(b)
    adjList[b].append(a) #undirected graph

#BFS
visited = [False] * (n+1)
parent = [-1] * (n+1) #for pathing

from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        u = q.popleft()
        for v in adjList[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)

bfs(1)

if not visited[n]:
    print('IMPOSSIBLE')
else:
    path = []
    curr = n
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    print(len(path))
    print(*path)