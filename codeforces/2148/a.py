t = int(input())

for i in range(t):
    x, n = map(int, input().split())
    res = 0
    for j in range(n):
        res += x
        x = -x
    print(res)

    