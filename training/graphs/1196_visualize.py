import heapq

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            #self.adj_matrix[v][u] = weight  # For undirected graph ONE WAY FLIGHTS

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

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances
    def k_shortest(self, start_idx, end_idx, k):
        """
        Multi-Dijkstra on an adjacency matrix:
        keep up to k best distances per node.
        """
        dist = [[] for _ in range(self.size)]
        pq = [(0, start_idx)]
        heappush, heappop = heapq.heappush, heapq.heappop

        while pq and len(dist[end_idx]) < k:
            d, u = heappop(pq)
            if len(dist[u]) >= k:
                continue
            dist[u].append(d)

            row = self.adj_matrix[u]
            for v in range(self.size):
                w = row[v]
                if w != 0 and len(dist[v]) < k:
                    heappush(pq, (d + w, v))

        return dist[end_idx]

n, m, k = map(int, input().split())

g = Graph(n)

for i in range(n):
    g.add_vertex_data(i, chr(ord('A') + i))

    




for i in range(m):
    a, b, c = map(int, input().split())

    g.add_edge(a-1, b-1, c)

#print the whole map
print("Adjacency Matrix:")
print("   ", end="")
for name in g.vertex_data:
    print(f"{name:>3}", end=" ")
print()
for i in range(n):
    print(f"{g.vertex_data[i]:>3}", end=" ")
    for j in range(n):
        print(f"{g.adj_matrix[i][j]:>3}", end=" ")
    print()

#print Dijkstra's algorithm from vertex A
distances = g.dijkstra('A')
print("\nDijkstra's Algorithm starting from vertex A:")
for i, d in enumerate(distances):
    print(f"Distance from A to {g.vertex_data[i]}: {d}")
    