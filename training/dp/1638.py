MOD = 10**9 + 7

n = int(input())
grid = []
for i in range(n):
    grid.append(input())

dp = [0] * (n+1)

for i in range(n):
    row = grid[i]
    for j in range(1, n+1):
        if row[j-1] == '*':
            dp[j] = 0
        else:
            if i == 0 and j == 1:
                dp[j] = 1
            else:
                dp[j] = (dp[j] + dp[j-1]) % MOD
print(dp[n])