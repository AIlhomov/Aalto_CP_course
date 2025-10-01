import sys
sys.setrecursionlimit(100000)

s = []
 
tsort = []
 
adj = [[] for i in range(100001)]
 
visited = [False for i in range(100001)]
 
def dfs(u):

    visited[u] = 1
    
    for it in adj[u]:
        if visited[it] == 1:
            return False
        elif visited[it] == 0:
            if not dfs(it):
                return False
 
    visited[u] = 2
    s.append(u)
    return True

def addEdge(u, v):  
    adj[u].append(v)

if __name__ == "__main__":
    
    n, m = map(int, input().split())

    
    for i in range(m):
        a, b = map(int, input().split())
        addEdge(a, b)
    
    posssible = True
    for i in range(1, n+1):
        if visited[i] == 0:
            if not dfs(i):
                posssible = False
                break

    if not posssible:
        print('IMPOSSIBLE')
    else:
        s.reverse()
        print(' '.join(map(str, s)))
        