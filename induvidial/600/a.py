n, m, k = map(int, input().split())
if m > 0:
    a = list(map(int, input().split()))



# n = circular track (n * 100 meters)
# m = boost pads (located at ai * 100 meters)
# k = seconds for how long she drives
# a = boost locations
meters = 0
j = 0
current_index = 0
if m != 0:
    for seconds in range(0, k):
        if current_index == n: #circular
            current_index = 1
        if j == m:
            j = 0
        if current_index == a[j]:
            j += 1
            meters += 200
        else:
            meters += 100
        current_index += 1
    print(meters % (n*100))
else:
    print(k*100 % (n*100))




