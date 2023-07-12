from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    visit = [[0]*M for _ in range(N)]
    visit[i][j] = 1
    dis = 0

    while dq:
        cx, cy = dq.popleft()
        for di in range(4):
            nx, ny = cx + dx[di], cy + dy[di]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if board[nx][ny] == 'W' or visit[nx][ny] != 0:
                continue
            dq.append((nx, ny))
            visit[nx][ny] = visit[cx][cy] + 1
            dis = max(dis, visit[nx][ny])
    return dis - 1


ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            ans = max(ans, bfs(i, j))
print(ans)
