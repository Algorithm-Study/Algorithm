dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
hx, hy = [-1, -1, 1, 1], [-1, 1, -1, 1]


def check(x, y):
    cnt = 0
    for di in range(4):
        nx, ny = x + dx[di], y + dy[di]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] > 0:
            cnt += 1
    return cnt


def grow():
    global board
    temp = [[0]*n for _ in range(n)]
    for w in wall:
        temp[w[0]][w[1]] = -1

    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                temp[i][j] = check(i, j) + board[i][j]
    board = temp


def breed():
    global board
    temp = [[0] * n for _ in range(n)]
    for w in wall:
        temp[w[0]][w[1]] = -1

    for i in range(n):
        for j in range(n):
            point = []
            if board[i][j] > 0:
                temp[i][j] = board[i][j]
                for di in range(4):
                    nx, ny = i + dx[di], j + dy[di]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if board[nx][ny] != 0:
                        continue
                    if herbicide[nx][ny] > 0:
                        continue
                    point.append((nx, ny))
            if len(point) > 0:
                tree = board[i][j] // len(point)
                for px, py in point:
                    temp[px][py] += tree
    board = temp


def herbicide_point():
    global ans
    max_tree = 0
    h_point = (0, 0)
    for i in range(n):
        for j in range(n):
            cnt = 0
            if board[i][j] > 0:
                cnt += board[i][j]
                for di in range(4):  # 4 방향으로
                    nx, ny = i, j
                    for _ in range(k):  # k칸 만큼 전파
                        nx, ny = nx + hx[di], ny + hy[di]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            break
                        if board[nx][ny] <= 0:
                            break
                        cnt += board[nx][ny]
            if cnt > max_tree:
                max_tree = cnt
                h_point = (i, j)
    ans += max_tree
    return h_point


def herbicide_injection(x, y):
    board[x][y] = 0
    herbicide[x][y] = c + 1
    for di in range(4):
        nx, ny = x, y
        for _ in range(k):
            nx, ny = nx + hx[di], ny + hy[di]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break
            if board[nx][ny] <= 0:
                herbicide[nx][ny] = c + 1
                break
            board[nx][ny] = 0
            herbicide[nx][ny] = c + 1

    for i in range(n):
        for j in range(n):
            if herbicide[i][j] > 0:
                herbicide[i][j] -= 1


n, m, k, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
herbicide = [[0]*n for _ in range(n)]
wall = []
for i in range(n):
    for j in range(n):
        if board[i][j] == -1:
            wall.append((i, j))
ans = 0
for _ in range(m):
    grow()
    breed()
    h_x, h_y = herbicide_point()
    herbicide_injection(h_x, h_y)
print(ans)
