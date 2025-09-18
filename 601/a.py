n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# n coins radius
# m holes radius
import bisect
from itertools import accumulate
res = []
pref = list(accumulate(b, max))
for coin in a:
    insertion_point = bisect.bisect_left(pref, coin)

    if insertion_point < m:
        hole_num = insertion_point + 1
    else:
        hole_num = m + 1
    res.append(hole_num)
print(*res)