import heapq, sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        minimum = float('inf')
        for node in range(self.V):
            print(node, "\t\t", dist[node])
            if dist[node] < minimum and dist[node] != 0:
                minimum = dist[node]
        print('here: ',minimum)
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = 1e7

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and 
                   sptSet[v] == False and 
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)
def dijkstra(graph, start, end):
  # Create a priority queue to store the nodes that need to be processed
    pq = []
      # Create a dictionary to store the distances from the start node to other nodes
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
      # Create a dictionary to store the previous node for each node
    previous = {node: None for node in graph}
    # Add the start node to the priority queue with a priority of 0
    heapq.heappush(pq, (0, start))
    # While there are nodes in the priority queue:
    while pq:
    # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)
    # If we have reached the end node, return the distances and previous nodes
    if current_node == end:
        return distances, previous
    # Iterate over the neighbors of the current node
    for neighbor, weight in graph[current_node].items():
      # Calculate the distance to the neighbor through the current node
      distance = current_distance + weight
      # If the distance to the neighbor through the current node is shorter than the current distance to the neighbor, update the distance and previous node
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        previous[neighbor] = current_node
        # Add the neighbor to the priority queue with the updated distance as the priority
        heapq.heappush(pq, (distance, neighbor))
    print(distances)
n, q = map(int, input().split())

g = Graph(n)
islands = []
for i in range(n):
    a = list(map(int, input().split()))
    islands.append(a)
g.graph = islands
print(islands)

for i in range(q):
    x, y = map(int, input().split())

    #g.dijkstra(x-1)
    dijkstra(islands, x, y)

    
