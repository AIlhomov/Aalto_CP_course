t = int(input())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

while t > 0:
    input()
    l = list(map(int, input().split()))

    for p in primes:
        if any(x % p != 0 for x in l):
            print(p)
            break
    else:
        print(-1)


    t -= 1