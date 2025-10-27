t = int(input())

def findMaxAverage(nums, k):
        currSum = sum(nums[:k])
        maxSum = currSum
        for i in range(k, len(nums)):
            currSum = currSum - nums[i - k] + nums[i]
            maxSum = max(maxSum, currSum)

        return maxSum // k

while t:

    n = int(input())
    a = list(map(int, input().split()))
    print(findMaxAverage(a, 1))
    t -= 1