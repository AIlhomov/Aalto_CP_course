n, k = map(int, input().split())

#n size of forest, k number of trees to cut
trees = list(range(1, n+1))
arr = []
trees.reverse()

def solve(n):
    
    #try to find the pairs
    for _ in range(k):
        for tree in trees:
            arr.append(tree)
            if sum(arr) % n == 0:
                return arr

if n == k:
    print(*trees)
elif k == 1:
    print(trees[0])
else:
    print(*solve(n))