n, m = map(int, input().split())    
adjList = [[] for _ in range(n+1)]


for i in range(m):
    a, b, c = map(int, input().split())

    adjList[a].append((b, c))

# djikstras:
import heapq

dist = [float('inf')] * (n+1)
dist[1] = 0

pq = [(0, 1)]

while pq:
    curr_dist, u = heapq.heappop(pq)
    if curr_dist > dist[u]:
        continue
    for v, w in adjList[u]:
        new_dist = curr_dist + w
        if new_dist < dist[v]:
            dist[v] = new_dist
            heapq.heappush(pq, (new_dist, v))
print(' '.join(map(str, dist[1:])))