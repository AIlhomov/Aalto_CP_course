import math
s = input()
n = len(s)
#print(math.perm(len(s), len(s) - len(set(s))))
#print(math.perm(n, 2))

s1 = set(s)

count = []
res = 1

for e in s1:
    #divide by all the duplicates in s
    
    s2 = s.count(e)
    count.append(s2)

    res *= math.factorial(s2)

print(math.factorial(n) // res)