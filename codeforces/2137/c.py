t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    test_a = a
    test_b = b
    res = -1
    if (a+b) % 2 == 0:
        res = max(a + b, res)
    for k in range(1, b+1):
        if b % k == 0: # divisible
            
            a *= k
            b = b // k
            if (a+b) % 2 == 0:
                res = max(a + b, res)
            else:
                a = test_a
                b = test_b
    print(res)