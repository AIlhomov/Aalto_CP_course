a, p = map(int, input().split())

if a > (p // 2):
    print('IMPOSSIBLE')
    raise SystemExit

# 1 4
# 2 6
# 3 8

def printall(a):
    print('POSSIBLE')
    print('0' * (a+2))
    print('0', '1' * a, '0', sep='')
    print('0' * (a+2))
    
if a == 1:
    if p == 4:
        printall(a)
        #print('POSSIBLE')
        #print('000\n010\n000')
    else:
        print('IMPOSSIBLE')
elif a == 2:
    if p == 6:
        printall(a)
        #print('POSSIBLE')
        #print('0000\n0110\n0000')
    else:
        print('IMPOSSIBLE')
elif a == 3:
    if p == 8:
        printall(a)
        #print('POSSIBLE')
        #print('00000\n01110\n00000')
    else:
        print('IMPOSSIBLE')
elif a == 4:
    if p == 8 or p == 10:
        printall(a)
        #print('POSSIBLE')
        #print('')
    else:
        print('IMPOSSIBLE')
elif a == 5:
    if p == 10:
        printall(a)
    else:
        print('IMPOSSIBLE')
elif a == 6:
    if p == 12 or p == 10:
        printall(a)
    else:
        print('IMPOSSIBLE')
