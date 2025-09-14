n, m = map(int, input().split())
x = list(map(int, input().split()))

MOD = 10**9 + 7

# dp has padding at ends to simplify neighbors
dp = [0] * (m + 2)

# initialize first position
if x[0] == 0:
    for v in range(1, m + 1):
        dp[v] = 1
else:
    dp[x[0]] = 1

for i in range(1, n):
    vfix = x[i]
    ndp = [0] * (m + 2)
    if vfix == 0:
        # any value allowed
        for v in range(1, m + 1):
            ndp[v] = (dp[v - 1] + dp[v] + dp[v + 1]) % MOD
    else:
        # only one value allowed
        v = vfix
        ndp[v] = (dp[v - 1] + dp[v] + dp[v + 1]) % MOD
    dp = ndp

# sum over valid values (works whether last is fixed or not)
print(sum(dp[1:m+1]) % MOD)