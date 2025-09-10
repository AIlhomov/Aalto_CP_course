for i in range(30):
    res = 2 ** i
    if res > 1000000:
        res = 0
    print(res, end=' ')