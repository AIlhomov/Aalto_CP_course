n, m = map(int, input().split())
labyrinth = []
sr = sc = -1
monsters = []

for i in range(n):
    row = input()
    labyrinth.append(row)
    for j in range(m):
        ch = row[j]
        if ch == 'A':
            sr, sc = i, j
        elif ch == 'M':
            monsters.append((i, j))
#bfs
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
ch = ('U', 'D', 'L', 'R')

# monsters:
distM = [[float('inf')]*m for _ in range(n)]
mq = deque()

#because monsters move we have to do 2bfs
while mq:
    r, c = mq.popleft()
    t = distM[r][c]
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and labyrinth[nr][nc] != '#' and \
        distM[nr][nc] == float('inf'):
            distM[nr][nc] = t + 1
            mq.append((nr, nc))

for r, c in monsters:
    distM[r][c] = 0
    mq.append((r, c))

q = deque()
q.append((sr, sc)) #start from a

distA = [[-1]*m for _ in range(n)]
parent = [[None]*m for _ in range(n)]
step = [[None]*m for _ in range(n)]

if r == 0 or r == n-1 or c == 0 or c == m-1 and 0 < distM[sr][sc]:
    print('YES')
    print(0)
    raise SystemExit

distA[sr][sc] = 0
found = False
end_r = end_c = -1



while q:
    r, c = q.popleft()
    t = distA[r][c]

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < n and 0 <= nc < m and labyrinth[nr][nc] != '#' \
        and distA[nr][nc] == -1:
            #we arrive at strictly earlier (t+1) than monsters
            if (t+1) < distM[nr][nc]:
                distA[nr][nc] = t + 1
                parent[nr][nc] = (r, c)
                step[nr][nc] = ch[k]
                q.append((nr, nc))
                if nr == 0 or nr == n-1 or nc == 0 or nc == m-1:
                    found = True
                    er, ec = nr, nc
                    q.clear()
                    break

if not found:
    print('NO')
else:
    #path
    path = []
    r, c = er, ec
    while (r, c) != (sr, sc):
        path.append(step[r][c])
        r, c = parent[r][c]
    path.reverse()
    print('YES')
    print(len(path))
    print(''.join(path))