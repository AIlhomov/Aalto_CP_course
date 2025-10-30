s = input()

def solve(s):
    l = r = 0
    n = len(s)
    z = [0] * n
    z[0] = n #only fix

    for i in range(1, n):
        if i > r:
            l = r = i
            while r < n and s[r] == s[r-l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            rel_ind = i-l
            if z[rel_ind] + i <= r:
                z[i] = z[rel_ind]
            else:
                l = i
                while r < n and s[r] == s[r-l]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z

print(*solve(s))
