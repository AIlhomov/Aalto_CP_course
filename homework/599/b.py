n = int(input())
x = list(map(int, input().split()))

if n < 3:
    print(0)
else:
    dp = [0] * (n+1)
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-3] + x[i-2])
    print(dp[n])