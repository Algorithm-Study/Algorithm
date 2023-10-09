from collections import deque

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

r, c = map(int, input().split())
dq = deque()
board = [list(input()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
sp, water = (0, 0), []

for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            sp = (i, j)
        elif board[i][j] == '*':
            water.append((i, j))

for wx, wy in water:
    dq.append(('w', wx, wy, 0))
    visit[wx][wy] = -1
dq.append(('b', sp[0], sp[1], 0))
visit[sp[0]][sp[1]] = 1

while dq:
    val, cx, cy, cnt = dq.popleft()
    for di in range(4):
        nx, ny = cx + dx[di], cy + dy[di]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:  # 범위를 넘어가면 넘어감
            continue
        if board[nx][ny] == 'X':  # 돌이면 넘어감
            continue
        if val == 'w':  # 물일 경우
            if board[nx][ny] == 'D' or visit[nx][ny] == -1:
                continue
            visit[nx][ny] = -1
            dq.append((val, nx, ny, cnt))
        elif val == 'b':
            if board[nx][ny] == '*' or visit[nx][ny] != 0:
                continue
            if board[nx][ny] == 'D':
                print(cnt + 1)
                exit()
            visit[nx][ny] = 1
            dq.append((val, nx, ny, cnt + 1))

print("KAKTUS")
