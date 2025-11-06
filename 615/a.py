s = input()
t = input()

n = len(s)
n2 = len(t)

if n2 > n:
    print('No')
    raise SystemExit

i = 0
j = 0


while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
        j += 1
    else:
        i += 1
#print(i, j)
if j == len(t):
    print('Yes')
else:
    print('No')
        