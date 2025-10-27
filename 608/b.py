from collections import defaultdict
# Recursive DFS function
def dfs_recursive(tree, node, end, path, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    visited.add(node)    # Mark the node as visited
    #print(node, end=' ')          # Print the current node (for illustration)
    path.append(node)
    if node == end:
        return path
    for child in tree[node]:  # Recursively visit children
        if child not in visited:
            dfs_recursive(tree, child, end, path, visited)

n, m = map(int, input().split())

adj = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    #adj[b].append(a)
path = []
print(dfs_recursive(adj, 1, n, path))
