n = int(input())
a = list(map(int, input().split()))

b = sorted(a)
res = 0

#make the map
c = {}

for i in range(len(a)):
    c[a[i]] = i #index: value
 
#print(c)
#print(c[a[0]])
#print(a, b)
for i in range(len(a)):
    if a[i] != b[i]:
        res += 1
        #k, l = a.index(a[i]), a.index(b[i])
        k, l = c[a[i]], c[b[i]]
        c[a[i]], c[b[i]] = l, k
        a[k], a[l] = a[l], a[k]
        #a[i] = b[b.index(a[i])]
print(res)