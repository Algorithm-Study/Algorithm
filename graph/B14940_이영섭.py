from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[-1]*m for _ in range(n)]
sx, sy = 0, 0
flag = False
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            sx, sy = i, j
            flag = True
            break
    if flag:
        break
dq = deque()
dq.append((sx, sy))
visit[sx][sy] = 0
while dq:
    cx, cy = dq.popleft()
    for dir in range(4):
        nx, ny = cx + dx[dir], cy + dy[dir]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if board[nx][ny] != 1 or visit[nx][ny] > 0:
            continue
        dq.append((nx, ny))
        visit[nx][ny] = visit[cx][cy] + 1
visit[sx][sy] = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            visit[i][j] = 0
        print(visit[i][j], end=' ')
    print()