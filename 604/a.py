n = input()
res = int(n)
count = 0
while res != 0:
    numbers = list(map(int, list(str(res))))
    findMax = max(numbers)
    res -= findMax
    count += 1
print(count)