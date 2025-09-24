n = int(input())
a = list(map(int, input().split()))

#for _ in range(n):
#    for i in range(len(a)-1):
#        if a[i] > a[i+1]:
#            a[i], a[i+1] = a[i+1], a[i]
#            res += 1
def count(arr):
    n = len(arr)

    # Stores the count
    count = 1

    # Stores the maximum
    maxi = arr[0]

    # Iterate over the array
    for i in range(1, n):

        # If an element greater
        # then maximum is obtained
        if arr[i] > maxi:

            # Increase count
            count += 1

            # Update maximum
            maxi = arr[i]

    return count

print(count(a))