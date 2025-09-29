MOD = 10**9 + 7

n = int(input())
songs = list(map(int, input().split()))
s = 0
count1 = 0
res = 0

for i in range(len(songs)):
    if songs[i] == 1:
        s += (s + 1) % MOD
        count1 += 1
    elif songs[i] == 2:
        s *= 2 % MOD
    else:
        res += s - count1
print(res)

