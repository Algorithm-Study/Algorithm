from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def ball_shoot(rd):
    global ball_path
    rd = rd % (4*n)
    if rd // n == 0:
        ball_path = [[rd % n, y] for y in range(n)]
    elif rd // n == 1:
        ball_path = [[x, rd % n] for x in range(n-1, -1, -1)]
    elif rd // n == 2:
        ball_path = [[n - 1 - rd % n, y] for y in range(n-1, -1, -1)]
    else:
        ball_path = [[x, n - 1 - rd % n] for x in range(n)]


def bfs(x, y):
    visit = [[0] * n for _ in range(n)]
    dq = deque()
    visit[x][y] = 1
    tp = deque([[x, y]])
    for di in range(4):
        nx, ny = x + dx[di], y + dy[di]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] == 2:
            dq.append((nx, ny))
            visit[nx][ny] = 1
            tp.append([nx, ny])
            break
    while dq:
        cur = dq.popleft()
        for di in range(4):
            nx, ny = cur[0] + dx[di], cur[1] + dy[di]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] == 0 or board[nx][ny] == 4 or visit[nx][ny] == 1:
                continue
            dq.append((nx, ny))
            visit[nx][ny] = 1
            tp.append([nx, ny])
    people.append(tp)


def init():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bfs(i, j)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3:
                board[i][j] = 4


def move_people():
    for p in people:
        for di in range(4):
            nx, ny = p[0][0] + dx[di], p[0][1] + dy[di]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if nx == p[1][0] and ny == p[1][1]:
                continue
            if board[nx][ny] == 4:
                p.appendleft([nx, ny])
                p.pop()
                break


def cal_score():
    for bp in ball_path:
        for p in people:
            for idx, bpp in enumerate(p):
                if bp == bpp:
                    p.reverse()
                    return (idx+1)**2
    return 0


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ball_path = []
people = []
init()
score = 0

for i in range(k):
    move_people()
    ball_shoot(i)
    score += cal_score()

print(score)
