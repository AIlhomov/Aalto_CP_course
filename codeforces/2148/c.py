t = int(input())
paces = []
for i in range(t):
    n, m = map(int, input().split())
    res = 0
    for j in range(n):
        a, b = map(int, input().split())
        paces.append([a,b])
    def valid(paces, side):
        return paces[j][1] == 1 and side == 1 or paces[j][1] == 0 and side == 0
    side = 0
    j = 0
    dontRun = False
    for curr in range(0, m):
        #always run
        side = curr % 2
        res += 1
        if curr + 1 == paces[j][0]: #future seeing
            if j != len(paces)-1: #dont even try to check last index
                j += 1
            #now lets check if its optimal to run back or stay
            if paces[j][1] == 1:
                if side == 1:
                    #stay
                    
                    dontRun = True
                    side = 1
                else: #run
                    res -= 1
                    side = 0
            elif paces[j][1] == 0:
                if side == 0:
                    #stay
                    
                    dontRun = True
                    side = 0
                else: #run
                    res -= 1
                    side = 1
        
        
        

        
    print(res)

    
    paces.clear()
