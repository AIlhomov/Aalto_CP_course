input()
x = list(map(int, input().split()))

x.sort()
currSum = 1

for c in x:
    if c > currSum:
        break
    currSum += c

print(currSum)