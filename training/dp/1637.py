n = int(input())
count = 0
while n != 0:
    all_num = [int(d) for d in str(n)]
    maximum = max(all_num)
    n -= int(maximum)
    count += 1
print(count)