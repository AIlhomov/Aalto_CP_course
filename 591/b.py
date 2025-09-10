n, m, k = map(int, input().split())
#the number of applicants, the number of apartments, 
# and the maximum allowed difference.
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
res = 0
#two pointers
i = 0
j = 0

while i < n and j < m:
    
    if a[i] - k > b[j]:
        j += 1
    elif a[i] + k < b[j]:
        i += 1
    else:
        #its a match!
        res += 1
        i += 1
        j += 1

print(res)
