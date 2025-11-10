import math

n = int(input())
lattice_points = [tuple(map(int, input().split())) for _ in range(n)]

s = 0  
b = 0  

for i in range(n):
    x1,y1 = lattice_points[i]
    x2,y2 = lattice_points[(i+1)%n]
    s += x1*y2 - x2*y1
    b += math.gcd(abs(x2-x1), abs(y2-y1))

s = abs(s)
i = (s - b + 2)//2
print(i, b)