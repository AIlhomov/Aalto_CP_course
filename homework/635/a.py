n = int(input())
MOD = 10** 9 + 7


for _ in range(n):
    a, b = map(int, input().split())

    print(pow(a, b, MOD))