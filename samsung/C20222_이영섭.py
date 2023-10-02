from collections import deque, defaultdict
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]


def bfs(x, y, visit, cnt):
    out_line, bd = [], 1
    dq = deque()
    dq.append((x, y))
    visit[x][y] = cnt
    while dq:
        cx, cy = dq.popleft()
        for di in range(4):
            nx, ny = cx + dx[di], cy + dy[di]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[x][y] != board[nx][ny]:
                out_line.append((nx, ny, visit[nx][ny]))
                continue
            if visit[nx][ny] > 0:
                continue
            bd += 1
            visit[nx][ny] = cnt
            dq.append((nx, ny))
    return bd, out_line


def art_point():
    visit = [[0] * n for _ in range(n)]
    line, point = defaultdict(list), defaultdict(list)
    cnt = 1
    for i in range(n):
        for j in range(n):
            if visit[i][j] > 0:
                continue
            point[cnt].append(board[i][j])
            bfs_point, bfs_line = bfs(i, j, visit, cnt)
            line[cnt] = bfs_line
            point[cnt].append(bfs_point)
            cnt += 1

    line_dict = [[0]*(len(line.keys()) + 1) for _ in range(len(line.keys()) + 1)]
    for li in line.keys():
        for idx, (x, y, v) in enumerate(line[li]):
            line_dict[li][visit[x][y]] += 1
            line_dict[visit[x][y]][li] += 1

    val = 0
    for i in range(1, len(line.keys()) + 1):
        for j in range(i + 1, len(line.keys()) + 1):
            val += (point[i][1] + point[j][1]) * point[i][0] * point[j][0] * (line_dict[i][j] // 2)

    return val


def rotate_cross():
    temp = [board[i][n//2] for i in range(n//2)]
    for i in range(n//2):
        board[i][n//2] = board[n//2][n - 1 - i]
    for i in range(n//2):
        board[n//2][n - 1 - i] = board[n - 1 - i][n//2]
    for i in range(n//2):
        board[n - 1 - i][n//2] = board[n//2][i]
    for i in range(n//2):
        board[n//2][i] = temp[i]


def rotate_left():
    plus = [0, n//2 + 1]
    for xp in plus:
        for yp in plus:
            temp = [[0]*(n//2) for _ in range(n//2)]
            for i in range(n//2):
                for j in range(n//2):
                    temp[i][j] = board[xp + n//2 - 1 - j][yp + i]
            for i in range(n//2):
                for j in range(n//2):
                    board[xp + i][yp + j] = temp[i][j]


n = int(input())  # n은 무조건 홀수
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

ans += art_point()
for _ in range(3):
    rotate_cross()
    rotate_left()
    ans += art_point()

print(ans)
