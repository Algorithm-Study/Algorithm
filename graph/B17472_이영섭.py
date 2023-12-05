from collections import deque

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]


def bfs(x, y, n):
    board[x][y] = n
    nl = [(x, y)]
    dq = deque([(x, y)])
    visit = [[0]*M for _ in range(N)]
    visit[x][y] = 1
    while dq:
        cx, cy = dq.popleft()
        for di in range(4):
            nx, ny = cx + dx[di], cy + dy[di]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if board[nx][ny] == 0 or visit[nx][ny] == 1:
                continue
            dq.append((nx, ny))
            board[nx][ny] = n
            nl.append((nx, ny))
            visit[nx][ny] = 1
    return nl


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ls = []

num = 2
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            ls.append(bfs(i, j, num))
            num += 1

edge = []
for il in ls:
    for x, y in il:
        for di in range(4):
            dist = 0
            nx = x + dx[di]
            ny = y + dy[di]
            while True:
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                dest = board[nx][ny]
                if board[x][y] == dest:
                    break
                if dest == 0:
                    nx += dx[di]
                    ny += dy[di]
                    dist += 1
                    continue
                if dist < 2:
                    break
                edge.append((dist, board[x][y], dest))
                break

edge.sort(reverse=True)
ans = 0
flag = 0
parents = [i for i in range(num)]


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    parents[y] = x


count = len(ls) - 1
while count:
    try:
        distance, a, b = edge.pop()
    except:
        flag = 1
        break
    if find(a) != find(b):
        union(a, b)
        ans += distance
        count -= 1

if flag == 1:
    print(-1)
else:
    print(ans)
