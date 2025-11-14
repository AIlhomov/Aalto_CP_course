a, m = map(int, input().split())

try:
    x = pow(a, -1, m)
    print(x)
except ValueError:
    print(-1)