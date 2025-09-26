t = int(input())
import itertools
while (t):

    input()
    a = list(map(int, input().split()))

    a.sort()
    res = []

    for i in range(0, len(a), 2):
        res.append(abs(a[i] - a[i+1]))
    print(max(res))
    t -= 1