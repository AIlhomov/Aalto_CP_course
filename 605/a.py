n = int(input())
road = list(map(int, input().split()))

bestL = bestR = bestDiff = 0
up = down = 0
dir = 1 if road[1] > road[0] else -1

sign = -1
start = 0

for i in range(1, n):

    
    if road[i] > road[i-1]:
        sign = 1
    else:
        sign = -1 #down
    if sign == dir:
        continue
    else:
        end = i - 1
        diff = abs(road[end] - road[start])
        if diff > bestDiff:
            bestL = start
            bestR = end
            bestDiff = diff
        start = i - 1
        dir = sign
diff = abs(road[n-1] - road[start])
if diff > bestDiff:
    bestL = start
    bestR = n - 1
    bestDiff = diff
print(bestL+1, bestR+1)