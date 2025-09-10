# --- Representation: adjacency list as dict: node -> set(neighbors) ---

def mis_greedy_adjlist(G):
    """
    Maximal Independent Set (greedy).
    G: dict {u: set(neighbors_of_u)} for an undirected simple graph.
    Returns a set I that is independent and maximal.
    Complexity: O(n + m) with adjacency lists.
    """
    I = set()
    blocked = {u: False for u in G}   # True once u is chosen or adjacent to a chosen vertex
    alive = set(G.keys())             # Optional: track remaining vertices

    # Arbitrary order is fine; you can sort for determinism if you like
    for u in list(G.keys()):
        if u in alive and not blocked[u]:
            # choose u
            I.add(u)
            blocked[u] = True
            # remove u and block its neighbors (mirrors "remove from V")
            if u in alive:
                alive.remove(u)
            for v in G[u]:
                blocked[v] = True
                alive.discard(v)
    return I

def is_independent(G, S):
    for u in S:
        for v in G[u]:
            if v in S:
                return False
    return True

def is_maximal(G, S):
    if not is_independent(G, S):
        return False
    # Every outside vertex must touch S
    outside = set(G.keys()) - set(S)
    for u in outside:
        if all((v not in S) for v in G[u]):
            return False
    return True
def mis_greedy_matrix(adj):
    """
    adj: 0/1 adjacency matrix (list of lists), undirected simple graph, n x n.
    Greedy MIS in O(n^2).
    """
    n = len(adj)
    I = set()
    removed = [False]*n

    for i in range(n):
        if removed[i]:
            continue
        # check if i has a neighbor in I
        has_neighbor_in_I = any(adj[i][j] and (j in I) for j in range(n))
        if not has_neighbor_in_I:
            I.add(i)
            # remove i and its neighbors
            removed[i] = True
            for j in range(n):
                if adj[i][j]:
                    removed[j] = True
    return I


# Build a tiny graph
G = {
    0: {1,2},
    1: {0,3},
    2: {0,3},
    3: {1,2,4},
    4: {3}
}
I = mis_greedy_adjlist(G)
print("I =", I, "independent?", is_independent(G, I), "maximal?", is_maximal(G, I))
