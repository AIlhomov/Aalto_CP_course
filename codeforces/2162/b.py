def is_palindrome(s):
    return s == s[::-1]

def solve():
    n = int(input())
    s = input().strip()
    
    # Try all possible subsequences by trying all combinations of
    # removing c0 zeros and c1 ones (in a non-decreasing way)
    # For non-decreasing: we take some 0s first, then some 1s
    
    # Count positions of 0s and 1s
    zeros = [i for i in range(n) if s[i] == '0']
    ones = [i for i in range(n) if s[i] == '1']
    
    # Try removing different numbers of 0s and 1s
    for num_zeros in range(len(zeros) + 1):
        for num_ones in range(len(ones) + 1):
            # Select first num_zeros 0s and first num_ones 1s
            selected_indices = zeros[:num_zeros] + ones[:num_ones]
            selected_indices.sort()
            
            # Build remaining string
            remaining = []
            selected_set = set(selected_indices)
            for i in range(n):
                if i not in selected_set:
                    remaining.append(s[i])
            
            remaining_str = ''.join(remaining)
            
            # Check if remaining is palindrome
            if is_palindrome(remaining_str):
                print(len(selected_indices))
                if len(selected_indices) > 0:
                    print(' '.join(str(i + 1) for i in selected_indices))
                return
    
    print(-1)

t = int(input())
for _ in range(t):
    solve()
