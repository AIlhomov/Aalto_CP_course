n, m = map(int, input().split())

friends = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())    
    friends[a].append(b)
    friends[b].append(a) #undirected graph

visited = [False] * (n+1)

from collections import deque

team = [0] * (n+1)

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True
    team[s] = 1
    while q:
        u = q.popleft()
        for v in friends[u]:
            if not visited[v]:
                visited[v] = True
                team[v] = 3 - team[u] #opposite team
                q.append(v)
            elif team[v] == team[u]:
                return False
    return True
check = False
for i in range(1, n+1):
    if not visited[i]:
        if not bfs(i):
            print('IMPOSSIBLE')
            raise SystemExit
print(*team[1:])
