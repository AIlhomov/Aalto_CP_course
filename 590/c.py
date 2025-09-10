n = int(input())

def dp(n, i, count):
    count += 1
    return dp(n, i+count, count)

print(dp(n, 0, 0))