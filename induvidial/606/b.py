import heapq

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

INF = 10**9

#djikstra but extra
distances = [0] * (n + 1)
distances[1] = INF

pq = [(-distances[1], 1)]

while pq:
    curr_dist, u = heapq.heappop(pq)
    curr_dist = -curr_dist

    if curr_dist < distances[u]:
        continue

    for v, w in adj[u]:
        new_dist = min(curr_dist, w)
        if new_dist > distances[v]:
            distances[v] = new_dist
            heapq.heappush(pq, (-new_dist, v))
print(' '.join(map(str, distances[2:])))