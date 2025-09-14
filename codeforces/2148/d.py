t = int(input())

def sorted_oddsevens(seq):
    sorted_seq = sorted(seq)
    evens = (x for x in sorted_seq if x % 2 == 0)
    odds = (x for x in sorted_seq if x % 2 != 0)
    return [(next(evens) if x % 2 == 0 else next(odds)) for x in seq]

for i in range(t):
    input()
    a = list(map(int, input().split()))
    
    even, odd = [], [] 

    for i in range(len(a)): 
        if a[i] % 2 == 0: 
            even.append(a[i]) 
        else:  
            odd.append(a[i])
    odd.sort(reverse=True)
    even.sort(reverse=True)
    res = 0
    if len(odd) == 0:
        res = 0
    elif len(odd) % 2 == 1:
        res = sum(even)
        res += sum(odd[0:len(odd) // 2 + 1])  
    elif len(odd) % 2 == 0:
        res = sum(even)
        res += sum(odd[0:len(odd) // 2])  
    print(res)