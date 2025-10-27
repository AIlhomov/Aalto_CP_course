n = int(input())

adj = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

from collections import deque
#BFS
if n == 1:
    print(0)
    raise SystemExit
def bfs(start, n):
    dist = [-1] * (n+1)
    q = deque()

    q.append(start)
    dist[start] = 0
    farthest = start
    max_dist = 0

    while q:
        node = q.popleft()
        for neighbour in adj[node]:
            if dist[neighbour] == -1:
                dist[neighbour] = dist[node] + 1
                q.append(neighbour)

                if dist[neighbour] > max_dist:
                    max_dist = dist[neighbour]
                    farthest = neighbour
    return farthest, max_dist

x, _ = bfs(1, n)
y, diameter = bfs(x, n)

print(diameter)
