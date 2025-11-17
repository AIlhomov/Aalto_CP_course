n, a, b = map(int, input().split())

MOD = 998244353

import math

k = b - a #total skittles

res = 0
#calculate factorial beforeahnd in an array
facts = [1]*(n+b+1)
for i in range(1,n+b+1):
   facts[i] = facts[i-1]*(i) % MOD

def binom(n,k):
    if n == k:
        return 1
    elif k == 1:
        return n
    elif k > n:
        return 0
    else:
        a = facts[n]
        b = facts[k] 
        c = facts[n-k]
        #return facts[n] * pow(facts[k] * facts[n - k] % MOD, MOD - 2, MOD) % MOD
        div = a * pow(b * c % MOD, -1, MOD)
        return div
    

for i in range(a, b+1):
    #print(math.comb(i+n-1, n-1))
    #res += math.comb(i+n-1, n-1) % MOD
    #res += fac[a-1] // fac[b] // (fac[a-1] - fac[b-1]) 
    res += binom(i+n-1, n-1) % MOD
print(res % MOD)



