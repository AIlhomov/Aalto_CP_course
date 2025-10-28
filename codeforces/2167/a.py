t = int(input())

while t > 0:

    a, b, c, d = map(int, input().split())

    if a == b == c == d:
        print('yes')
    else:
        print('no')


    t -= 1