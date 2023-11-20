from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
dq = deque()

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            dq.append((i, j))
            visit[i][j] = 1

while dq:
    cx, cy = dq.popleft()
    for di in range(4):
        nx, ny = cx + dx[di], cy + dy[di]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == -1 or (visit[nx][ny] != 0 and visit[nx][ny] <= visit[cx][cy] + 1):
            continue
        visit[nx][ny] = visit[cx][cy] + 1
        dq.append((nx, ny))

cnt, max_val = 0, 0
for i in range(N):
    for j in range(M):
        if visit[i][j] > max_val:
            max_val = visit[i][j]
        elif board[i][j] != -1 and visit[i][j] == 0:
            cnt += 1

if cnt != 0:
    print(-1)
else:
    print(max_val - 1)
