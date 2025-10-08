n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    w = 0 if c == 1 else 1
    adj[a].append((b, w))
    adj[b].append((a, w))

lab = [-1] * (n + 1)

from collections import deque

def bfs(start):
    lab[start] = 0
    dq = deque([start])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            expect = lab[u] ^ w
            if lab[v] == -1:
                lab[v] = expect
                dq.append(v)
            elif lab[v] != expect:
                return False
    return True

ok = True
for u in range(1, n + 1):
    if lab[u] == -1:
        if not bfs(u):
            ok = False
            break

print("Yes" if ok else "No")