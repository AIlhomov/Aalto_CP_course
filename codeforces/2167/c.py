t = int(input())

while t > 0:

    n = int(input())
    mylist = list(map(int,input().split()))

    s = sorted(mylist)

    even = any(x % 2 == 0 for x in mylist)
    odd = any(x % 2 == 1 for x in mylist)
    if even and odd:
        print(*s)
    else:
        print(*mylist)

    t -= 1