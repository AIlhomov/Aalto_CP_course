n, m = map(int, input().split())
adjList = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())

    adjList[a].append(b)
    adjList[b].append(a) #undirected


#dfs for this one
visited = [False] * (n+1)
idx = [0] * (n+1) #next neighbour
parent = [-1] * (n+1) # for path

def solve(u, v):
    path = [u]
    x = u

    while x != v:
        x = parent[x]
        path.append(x)
    path.append(path[0])
    print(len(path))
    print(*path)
    raise SystemExit

for s in range(1, n+1):
    if visited[s]:
        continue
    #dfs 
    stack = [s]
    visited[s] = True
    parent[s] = -1
    idx[s] = 0
    while stack:
        u = stack[-1]
        if idx[u] == len(adjList[u]):
            stack.pop()
            continue
        v = adjList[u][idx[u]]
        idx[u] += 1
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            idx[v] = 0
            stack.append(v)
        elif v != parent[u]:
            solve(u, v)
print('IMPOSSIBLE')

