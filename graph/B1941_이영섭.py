from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

board = [list(input()) for _ in range(5)]


def bfs(p7):
    visit = [[1] * 5 for _ in range(5)]
    for x, y in p7:
        visit[x][y] = 0
    dq = deque()
    dq.append(p7[0])
    visit[p7[0][0]][p7[0][1]] = 1
    visit_num = 1

    while dq:
        cx, cy = dq.popleft()
        for di in range(4):
            nx, ny = cx + dx[di], cy + dy[di]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            if not visit[nx][ny]:
                visit[nx][ny] = 1
                visit_num += 1
                dq.append((nx, ny))

    if visit_num != 7:
        return False
    else:
        return True


def dfs(x, y, cnt):
    global ans
    if cnt >= 4:
        return
    if len(princess) == 7:
        if bfs(princess):
            ans += 1
        return
    for i in range(x * 5 + y, 25):
        nx = i // 5
        ny = i % 5
        princess.append((nx, ny))
        dfs(nx, ny, cnt + (board[nx][ny] == 'Y'))
        princess.pop()


ans = 0
for i in range(5):
    for j in range(5):
        princess = [(i, j)]
        if board[i][j] == 'S':
            dfs(i, j, 0)
        else:
            dfs(i, j, 1)
print(ans)
