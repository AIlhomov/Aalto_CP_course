t = int(input())

for i in range(t):
    n = int(input())    
    p = list(map(int,input().split()))

    for j in range(len(p)):
        print(p[i] + 2 - j, end=' ')
    print()