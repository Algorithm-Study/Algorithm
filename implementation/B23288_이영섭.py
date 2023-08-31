from collections import deque


def get_point(x, y):
    # 주사위가 도착한 칸에 대한 점수를 획득
    visit = [[0] * M for _ in range(N)]
    dq = deque()
    dq.append((x, y))
    val = board[x][y]
    visit[x][y] = 1
    cnt = 1
    while dq:
        cx, cy = dq.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if board[nx][ny] != val or visit[nx][ny] > 0:
                continue
            dq.append((nx, ny))
            cnt += 1
            visit[nx][ny] = 1
    return cnt * val


def dice_move(x, y):
    # 이동 방향으로 한 칸 굴러가고 없으면 반대로 굴러감
    global dice
    global dir
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        dir = (dir + 2) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
    temp = []
    if dir == 0:
        temp = [dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]]
        dice = temp[:]
    elif dir == 1:
        temp = [dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]]
        dice = temp[:]
    elif dir == 2:
        temp = [dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]]
        dice = temp[:]
    elif dir == 3:
        temp = [dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]]
        dice = temp[:]
    return nx, ny


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice = [1, 2, 3, 5, 4, 6] # 위, 북, 동, 남, 서, 아래
dir = 0
point = 0
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
x, y = 0, 0
for _ in range(K):
    x, y = dice_move(x, y)
    point += get_point(x, y)
    if dice[5] > board[x][y]:
        dir = (dir + 1) % 4
    elif dice[5] < board[x][y]:
        dir = (dir - 1) % 4
print(point)
