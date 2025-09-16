t = int(input())
MOD = 10**9+7
dp = [[0] * 2 for _ in range(1000002)]
# dp[i][0] - number of ways to add rectangles to the 2*i squares such that the last 2 squares are united
# dp[i][1] - number of ways to add rectangles to the 2*i squares such that the last 2 squares are NOT united
dp[1][0] = dp[1][1] = 1

for i in range(1, 1000000):
    dp[i][0] %= MOD
    dp[i][1] %= MOD
    dp[i+1][0] += 2*dp[i][0]
    dp[i+1][1] += dp[i][0]
    dp[i+1][0] += dp[i][1]
    dp[i+1][1] += 4*dp[i][1]

for i in range(t):
    n = int(input())

    ans = dp[n][0] + dp[n][1]
    ans %= MOD
    print(ans)