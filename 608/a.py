def solve(arr, X, N):

    vec = [[arr[i], i + 1] for i in range(N)]

    vec.sort()

    for ptr1 in range(N - 2):
        ptr2 = ptr1 + 1
        ptr3 = N - 1

        while ptr2 < ptr3:
            currSum = vec[ptr1][0] + vec[ptr2][0] + vec[ptr3][0]

            if currSum == X:
                print(vec[ptr1][1], vec[ptr2][1], vec[ptr3][1])
                return
            elif currSum > X:
                ptr3 -= 1
            elif currSum < X:
                ptr2 += 1

    print("IMPOSSIBLE")


n, x = map(int, input().split())
a = list(map(int, input().split()))

solve(a, x, n)