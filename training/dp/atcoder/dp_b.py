n, k = map(int, input().split())
h = list(map(int, input().split()))

INF = 10**18
dp = [INF] * n
dp[0] = 0

for i in range(1, n):
    hi = h[i]
    best = INF
    lo = i - k
    if lo < 0:
        lo = 0
    for j in range(lo, i):
        cost = dp[j] + (hi - h[j] if hi >= h[j] else h[j] - hi) #abs but faster
        if cost < best:
            best = cost
    dp[i] = best

print(dp[-1])