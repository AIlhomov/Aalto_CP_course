# Source - https://stackoverflow.com/questions/38840902/how-do-i-find-largest-valid-sequence-of-parentheses-and-brackets-in-a-string
# Posted by Paul Hankin
# Retrieved 11/5/2025, License - CC BY-SA 3.0

def longest_valid(s):
    match = [0] * (len(s) + 1)
    for i in range(1, len(s)):
        if s[i] in '({[':
            continue
        open = '({['[')}]'.index(s[i])]
        start = i - 1 - match[i - 1]
        if start < 0: continue
        if s[start] != open: continue
        match[i] = i - start + 1 + match[start - 1]
    best = max(match)
    end = match.index(best)
    return s[end + 1 - best:end + 1]

s = input() 
s2 = longest_valid(s)
if s2 == "":
    print(-1)
else:
    print(s2)
