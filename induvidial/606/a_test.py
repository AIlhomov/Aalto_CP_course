n, q = map(int, input().split())
k = list(map(int, input().split()))
x = list(map(int, input().split()))



for i in range(q):
    initial_key = x[i]
    inmate = k[initial_key-1]

    res = 1
    while initial_key != inmate:

        inmate = k[inmate-1]

        res += 1
    print(res, end=' ')
