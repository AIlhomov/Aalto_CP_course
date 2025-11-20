n, x = map(int, input().split())
a = list(map(int, input().split()))

Map = {0: 1}
currSum = 0
res = 0

for i in range(len(a)):

    currSum += a[i]

    if (currSum - x) in Map:
        res += Map[currSum - x]
    
    if currSum in Map:
        Map[currSum] += 1
    else:
        Map[currSum] = 1

print(res)
