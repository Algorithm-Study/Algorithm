from collections import deque

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
x, y = x - 1, y - 1

dq = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            dq.append((board[i][j], i, j))
dq.sort()
dq = deque(dq)

if board[x][y] != 0:
    print(board[x][y])
    exit()

for _ in range(s):
    new_dq = deque()
    while dq:
        virus, cx, cy = dq.popleft()
        for di in range(4):
            nx, ny = cx + dx[di], cy + dy[di]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] == 0:
                if nx == x and ny == y:
                    print(virus)
                    exit()
                board[nx][ny] = virus
                new_dq.append((virus, nx, ny))
    dq = new_dq.copy()
print(0)
