n, m, k = map(int, input().split())
if m > 0:
    a = list(map(int, input().split()))
    pads = [False] * (n)
    for pad in a:
        pads[pad] = True
    #print(pads)

    j = 0
    next_speed = 0

    for second in range(k+1):
        j = (j + next_speed) % n
        if pads[j] == True:
            next_speed = 2
        else:
            next_speed = 1
        #print(second, j)
    print(j * 100)


else:
    print((k*100) % (n*100))