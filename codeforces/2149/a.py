t = int(input())

while (t):
    input()
    a = list(map(int, input().split()))
    b = a.count(0)
    c = a.count(-1)

    if c % 2 == 1:
        print(b + 2)
    else:
        print(b)

    t -= 1