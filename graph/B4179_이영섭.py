from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visit = [[0]*C for _ in range(R)]
dq = deque()


def find_start_point(ch):
    for i in range(R):
        for j in range(C):
            if board[i][j] == ch:
                dq.append((i, j))
                visit[i][j] = 1


find_start_point('F')
while dq:
    cx, cy = dq.popleft()
    for di in range(4):
        nx, ny = cx + dx[di], cy + dy[di]
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        if visit[nx][ny] != 0 or board[nx][ny] == '#':
            continue
        dq.append((nx, ny))
        visit[nx][ny] = visit[cx][cy] + 1

find_start_point('J')
while dq:
    cx, cy = dq.popleft()
    for di in range(4):
        nx, ny = cx + dx[di], cy + dy[di]
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            print(visit[cx][cy])
            exit()
        if 0 < visit[nx][ny] <= visit[cx][cy] + 1 or board[nx][ny] != '.':
            continue
        dq.append((nx, ny))
        visit[nx][ny] = visit[cx][cy] + 1
print('IMPOSSIBLE')