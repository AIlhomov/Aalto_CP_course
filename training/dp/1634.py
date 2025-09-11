n, x = map(int, input().split())
coins = list(map(int, input().split()))

INF = 10**9
from collections import deque
#bfs and dp solve
def solve(x, coins):
    dp = [INF] * (x+1)
    dp[0] = 0
    q = deque([0])
    while q:
        curr_sum = q.popleft()
        if curr_sum == x:
            return dp[x]
        for coin in coins:
            new_sum = curr_sum + coin
            if new_sum <= x and dp[new_sum] == INF:
                dp[new_sum] = dp[curr_sum] + 1
                q.append(new_sum)
    return -1
print(solve(x, coins))