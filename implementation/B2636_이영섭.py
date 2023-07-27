from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

time, cheese = 0, 0
while True:
    time += 1
    dq = deque()
    visit = [[0]*m for _ in range(n)]
    dq.append((0, 0))
    visit[0][0] = 1
    cnt = 0
    while dq:
        cx, cy = dq.popleft()
        for di in range(4):
            nx, ny = cx + dx[di], cy + dy[di]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if board[nx][ny] == 0:
                visit[nx][ny] = 1
                dq.append((nx, ny))
            else:
                board[nx][ny] = 0
                cnt += 1
                visit[nx][ny] = 1
    if cnt == 0:
        break
    else:
        cheese = cnt

print(time - 1)
print(cheese)
