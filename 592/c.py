n, m = map(int, input().split())
labyrinth = []
sr = sc = -1
br = bc = -1

for i in range(n):
    row = input()
    labyrinth.append(row)
    for j in range(m):
        ch = row[j]
        if ch == 'A':
            sr, sc = i, j
        elif ch == 'B':
            br, bc = i, j

from collections import deque

q = deque()
q.append((sr, sc))

visited = [[False] * m for _ in range(n)]
parent = [[None]*m for _ in range(n)]
step = [[None]*m for _ in range(n)]

visited[sr][sc] = True
found = False
end_r = end_c = -1

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
ch = ('U', 'D', 'L', 'R')

while q:
    r, c = q.popleft()

    if labyrinth[r][c] == 'B':
        found = True
        end_r, end_c = r, c
        break

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and \
        labyrinth[nr][nc] != '#':
            visited[nr][nc] = True
            parent[nr][nc] = (r, c)
            step[nr][nc] = ch[i]
            q.append((nr, nc))

if not found:
    print('NO')
else:
    #its a yes so print the whole path
    path = []
    r, c = end_r, end_c

    while (r, c) != (sr, sc):
        path.append(step[r][c])
        r, c = parent[r][c]
    path.reverse()
    print('YES')
    print(len(path))
    print(''.join(path))