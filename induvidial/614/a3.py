n, m = map(int, input().split())


if (n * m) % 2 != 0:
    print(-1)
else:
    res = ""
    if n % 2 == 0:
        #print('YES')

        appendthis = 'D' * (n-1)
        res += appendthis
        
        appendthis = 'R' * (m-1)
        res += appendthis

        
        for i in range(n-2):
            res += 'U'
            if i % 2 == 0:
                appendthis = 'L' * (m-2)
                res += appendthis
                
            else:
                appendthis = 'R' * (m-2)
                res += appendthis
                
        res += 'U'
        for i in range(m-1):
            res += 'L'
    else:
        #print('NO')
        appendthis = 'R' * (m-1)
        res += appendthis
        
        appendthis = 'D' * (n-1)
        res += appendthis
        
        #res += '\n'
        for i in range(m-2):
            res += 'L'
            if i % 2 == 0:
                appendthis = 'U' * (n-2)
                res += appendthis
                
            else:
                appendthis = 'D' * (n-2)
                res += appendthis
                
        res += 'L'
        for i in range(n-1):
            res += 'U'
    print(res)