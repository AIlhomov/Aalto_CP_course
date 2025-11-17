import math

n, q = map(int, input().split())

for i in range(q):
    a, b = map(int, input().split())

    print(n // math.gcd(a, n))

