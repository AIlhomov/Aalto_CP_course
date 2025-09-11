n = int(input())
MOD = 10**9 + 7
 
def dp(n):
    memo = [0] * (n+1)
    memo[0] = 1
 
    for i in range(1, n+1):
        for j in range(1, 7):# dice face
            if i - j >= 0:
                memo[i] = (memo[i] + memo[i-j]) % MOD
    return memo[n]
 
print(dp(n))