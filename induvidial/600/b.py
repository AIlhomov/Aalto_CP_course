n = int(input())
x = list(map(int, input().split()))

res = x[0]
maxEnd = x[0]

for i in range(1, n):
    maxEnd = max(maxEnd + x[i], x[i])
    res = max(res, maxEnd)
print(res)