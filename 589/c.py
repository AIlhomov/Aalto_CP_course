n = int(input())
#event sweeping (timelapse)
MAX = 604802
diff = [0] * MAX #for overflow issues
curr = 0
best = 0
for i in range(n):
    l, r = map(int,input().split())

    diff[l] += 1
    diff[r+1] -= 1

for t in range(1, 604800 + 1):
    curr += diff[t]
    best = max(curr, best)

print(best)
