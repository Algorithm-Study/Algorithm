from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs_basecamp(i, j):
    dq = deque()
    visit = [[0]*n for _ in range(n)]
    dq.append((i, j))
    visit[i][j] = 1
    while dq:
        cx, cy = dq.popleft()
        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] == 1:
                return nx, ny
            if board[nx][ny] == 2 or visit[nx][ny] > 0:
                continue
            dq.append((nx, ny))
            visit[nx][ny] = visit[cx][cy] + 1


def bfs_move(i, j, di, dj):
    visit = [[0]*n for _ in range(n)]
    dq = deque()
    dq.append((i, j))
    visit[i][j] = 1
    while dq:
        cx, cy = dq.popleft()
        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if nx == di and ny == dj:
                return cx, cy
            if board[nx][ny] == 2 or visit[nx][ny] == 1:
                continue
            dq.append((nx, ny))
            visit[nx][ny] = 1


def move_people():
    for i in range(len(people_list)):
        if people_list[i] != 'EMPTY':
            cx, cy = people_list[i]  # 현재 지점
            cvx, cvy = cvs_list[i]  # 목적지
            nx, ny = bfs_move(cvx, cvy, cx, cy)  # 다음에 가야 하는 지점
            people_list[i] = (nx, ny)


def check_des():
    ans = 0
    for i in range(len(people_list)):
        if people_list[i] != 'EMPTY':
            if people_list[i] == cvs_list[i]:
                ans += 1
                board[people_list[i][0]][people_list[i][1]] = 2
                people_list[i] = 'EMPTY'
    return ans


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
people_list = []
basecamp = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            basecamp.append((i, j))
cvs_list = []
for i in range(m):
    x, y = map(int, input().split())
    cvs_list.append((x-1, y-1))
time = 0
end = 0
while True:
    time += 1
    # 1
    move_people()
    # 2
    end += check_des()
    # 3
    if time <= m:
        # 베이스 캠프로 들어감
        bx, by = bfs_basecamp(cvs_list[time-1][0], cvs_list[time-1][1])
        people_list.append((bx, by))
        board[bx][by] = 2
    if end == m:
        print(time)
        break

    # 모두 편의점에 들어간다면 time을 출력하고 break