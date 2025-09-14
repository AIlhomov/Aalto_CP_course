n = int(input())
h = list(map(int, input().split()))

dp = [0] * (n+1)
if n == 1:
    print(0)
    raise SystemExit
prev1 = abs(h[1] - h[0])
prev2 = 0

for i in range(2, n):
    cur = min(prev1 + abs(h[i] - h[i-1]),
              prev2 + abs(h[i] - h[i-2]))
    prev2, prev1 = prev1, cur
print(prev1)