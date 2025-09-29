n = int(input())
total = 0
i = 0
 
while (1 << i) <= n:
    cycle_lenght = 1 << (i + 1)
    cycles = (n + 1) // cycle_lenght
    k = (n + 1) % cycle_lenght
    total += cycles * (1 << i) + max(0, k - (1 << i))
    i += 1
 
print(total)