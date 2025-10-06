import heapq
from collections import defaultdict
class Graph:
    def __init__(self, size):
        self.adj_matrix = [defaultdict(int) for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight # directed graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i
            if u is None:
                break
            visited[u] = True
            for v, w in self.adj_matrix[u].items():
                if not visited[v]:
                    alt = distances[u] + w
                    if alt < distances[v]:
                        distances[v] = alt
        return distances

    def k_shortest(self, start_idx, end_idx, k):
        dist = [[] for _ in range(self.size)]
        pq = [(0, start_idx)]
        heappush, heappop = heapq.heappush, heapq.heappop

        while pq and len(dist[end_idx]) < k:
            d, u = heappop(pq)
            if len(dist[u]) >= k:
                continue
            dist[u].append(d)

            for v, w in self.adj_matrix[u].items():
                if len(dist[v]) < k:
                    heappush(pq, (d + w, v))

        return dist[end_idx]
    
n, m, k = map(int, input().split())

g = Graph(n)

for _ in range(m):
    u, v, w = map(int, input().split())
    g.add_edge(u - 1, v - 1, w)

ans = g.k_shortest(0, n - 1, k)
print(' '.join(map(str, ans)))