from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]
visit = [[[0]*100 for _ in range(n)] for _ in range(n)]
dq = deque()

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

dq.append((0, 0, 0))
visit[0][0][0] = 1
ans = float('inf')

while dq:
    cx, cy, cnt = dq.popleft()
    if cnt >= ans:
        continue
    if cx == n-1 and cy == n-1 and ans > cnt:
        ans = cnt
        continue
    for di in range(4):
        nx, ny = cx + dx[di], cy + dy[di]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] == '0' and not visit[nx][ny][cnt+1]:
            dq.append((nx, ny, cnt+1))
            visit[nx][ny][cnt+1] = 1
        elif board[nx][ny] == '1' and not visit[nx][ny][cnt]:
            dq.append((nx, ny, cnt))
            visit[nx][ny][cnt] = 1
print(ans)