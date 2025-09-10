n, m = map(int, input().split())

adjList = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())

    adjList[a].append((b, c))

#bellman ford:
dist = [0] * (n+1)
parent = [-1] * (n+1)

relaxed = -1
for i in range(n):
    relaxed = -1
    for u in range(1, n+1):
        du = dist[u]
        for v, w in adjList[u]:
            if du + w < dist[v]:
                dist[v] = du + w
                parent[v] = u
                relaxed = v
if relaxed == -1:
    print('NO')
    raise SystemExit

#jump into cycle
v = relaxed
for _ in range(n):
    v = parent[v]

cycle = []
u = v
while True:
    cycle.append(u)
    u = parent[u]
    if u == v:
        break
cycle.append(v) #close
cycle.reverse()

print('YES')
print(*cycle)