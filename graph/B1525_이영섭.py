from collections import defaultdict, deque


def find_zero():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j


dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

board = tuple([tuple(map(int, input().split())) for _ in range(3)])
ans_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

if [[board[i][j] for j in range(3)] for i in range(3)] == ans_board:
    print(0)
    exit()

zx, zy = find_zero()

dq = deque()
visit = defaultdict(int)

dq.append([board, zx, zy, 0])
visit[board] = 1

while dq:
    cur, cx, cy, cnt = dq.popleft()
    for di in range(4):
        nx, ny = cx + dx[di], cy + dy[di]

        if nx < 0 or ny < 0 or nx >= 3 or ny >= 3:
            continue

        list_cur = [[cur[i][j] for j in range(3)] for i in range(3)]

        tp = list_cur[cx][cy]
        list_cur[cx][cy] = list_cur[nx][ny]
        list_cur[nx][ny] = tp

        if list_cur == ans_board:
            print(cnt + 1)
            exit()

        tuple_cur = tuple([tuple(list_cur[i]) for i in range(3)])
        if visit[tuple_cur]:
            continue

        dq.append([tuple_cur, nx, ny, cnt+1])
        visit[tuple_cur] = 1
print(-1)
