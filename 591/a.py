n, m = map(int, input().split())

adjList = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a) #undirected graph

visited = [False] * (n+1)
soFar = []

def dfs(s, visited):
    stack = [s]
    visited[s] = True
    while stack:
        u = stack.pop()
        for v in adjList[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

for city in range(1, n+1):
    if not visited[city]:
        soFar.append(city)
        dfs(city, visited)
        
print(len(soFar)-1)
for i in range(len(soFar)-1):
    print(soFar[i], soFar[i+1])