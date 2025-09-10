n = int(input())
b = list(map(int, input().split()))

def binarySearch(b):
    left = ans = 0
    right = sum(b) // n

    def ok(x):
        need = 0
        give = 0
        for bi in b:
            if bi < x:
                need += x - bi
            else:
                give += (bi-x) // 2
        return give >= need

    while left <= right:
        mid = (left + right) // 2

        if ok(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans

        
print(binarySearch(b))