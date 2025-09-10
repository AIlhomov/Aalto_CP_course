t = int(input())

for i in range(t):
    k, x = map(int, input().split())
    for j in range(k):
        x *= 2
    print(int(x))