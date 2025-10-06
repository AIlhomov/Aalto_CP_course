n, q = map(int, input().split())
k = list(map(int, input().split()))
x = list(map(int, input().split()))

#loop through k and all of them are cycles, but count the steps and save in a map.

loops = {}

for i in range(n):
    start = i + 1
    if start in loops:
        continue
    count = 1
    weAreHere = k[i]
    visited = {start}
    while weAreHere != start and weAreHere not in visited:
        visited.add(weAreHere)
        weAreHere = k[weAreHere - 1]
        count += 1
    for v in visited:
        loops[v] = count
        

for i in range(q):
    print(loops[x[i]], end=' ')