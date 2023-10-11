from collections import deque

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

board = [[0]*501 for _ in range(501)]

n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2)+1):
        for j in range(min(y1, y2), max(y1, y2)+1):
            board[i][j] = -1

m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            board[i][j] = -2

dq = deque()
visit = [[0]*501 for _ in range(501)]
dq.append((0, 0, 0))
visit[0][0] = 1

while dq:
    cx, cy, cnt = dq.popleft()
    if cx == 500 and cy == 500:
        print(cnt)
        exit()
    for di in range(4):
        nx, ny = cx + dx[di], cy + dy[di]
        if nx < 0 or nx >= 501 or ny < 0 or ny >= 501:
            continue
        if visit[nx][ny] > 0 or board[nx][ny] == -2:
            continue
        if board[nx][ny] == -1:
            dq.append((nx, ny, cnt + 1))
        else:
            dq.appendleft((nx, ny, cnt))
        visit[nx][ny] = 1
print(-1)
