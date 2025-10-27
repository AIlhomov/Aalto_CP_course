import sys
it = sys.stdin.buffer.readline
n = int(input())
res = []

for i in range(n):
    a = int(input())
    res.append(str(a+1))
sys.stdout.write("\n".join(res))