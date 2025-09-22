n, x = map(int, input().split())
a = list(map(int, input().split()))
import collections

def longestSubarray(A, limit):
    maxd = collections.deque()
    mind = collections.deque()
    i = 0
    for a in A:
        while len(maxd) and a > maxd[-1]: maxd.pop()
        while len(mind) and a < mind[-1]: mind.pop()
        maxd.append(a)
        mind.append(a)
        if maxd[0] - mind[0] > limit:
            if maxd[0] == A[i]: maxd.popleft()
            if mind[0] == A[i]: mind.popleft()
            i += 1
    return len(A) - i, i

def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

ans = longestSubarray(a, x)
print(ans[1]+1,ans[0]) #index, length