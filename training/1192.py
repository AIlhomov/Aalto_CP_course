n, m = map(int, input().split())
grid = []
visited = [[False] * m for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #left right down up

for i in range(n):
    grid.append(input())

def in_bounds(r, c):
    return 0 <= r < n and 0 <= c < m

def neighbours(r, c):
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if in_bounds(nr, nc) and grid[nr][nc] == '.':
            yield nr, nc

def flood(sr, sc):
    stack = [[sr, sc]]
    visited[sr][sc] = True

    while stack:
        r, c = stack.pop()
        for (nr, nc) in neighbours(r, c):
            if not visited[nr][nc]:
                visited[nr][nc] = True
                stack.append((nr, nc))

rooms = 0

for r in range(n):
    for c in range(m):
        if grid[r][c] == '.' and not visited[r][c]:
            flood(r, c)
            rooms += 1
print(rooms)