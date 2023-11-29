from collections import deque

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

board = [list(input()) for _ in range(N)]

rnd = 1
while True:
    dq = deque([(x1, y1)])
    visit = [[0] * M for _ in range(N)]
    visit[x1][y1] = 1
    friend = []

    while dq:
        cx, cy = dq.popleft()
        for di in range(4):
            nx, ny = cx + dx[di], cy + dy[di]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or visit[nx][ny] == 1:
                continue
            if nx == x2 and ny == y2:
                print(rnd)
                exit()
            if board[nx][ny] == '1':
                visit[nx][ny] = 1
                friend.append((nx, ny))
            elif board[nx][ny] == '0':
                dq.append((nx, ny))
                visit[nx][ny] = 1

    for fx, fy in friend:
        board[fx][fy] = '0'

    rnd += 1
