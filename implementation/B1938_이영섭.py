from collections import deque


def get_dir(arr):
    if arr[0][0] == arr[1][0] == arr[2][0]:
        return 0  # -
    elif arr[2][1] - arr[0][1] == 2:
        return 1  # \
    elif arr[0][1] == arr[1][1] == arr[2][1]:
        return 2  # |
    elif arr[2][1] - arr[0][1] == -2:
        return 3  # /


def can_turn(x, y):
    for ix in range(x-1, x+2):
        for iy in range(y-1, y+2):
            if ix < 0 or ix >= N or iy < 0 or iy >= N:
                return False
            elif board[ix][iy] == '1':
                return False
    return True


def check(x, y, dir):
    if dir == 0:  # -
        if x < 0 or x >= N or y - 1 < 0 or y + 1 >= N:
            return False
        elif board[x][y-1] == '1' or board[x][y] == '1' or board[x][y+1] == '1':
            return False
        else:
            return True
    elif dir == 1:  # \
        if x - 1 < 0 or x + 1 >= N or y - 1 < 0 or y + 1 >= N:
            return False
        elif board[x-1][y-1] == '1' or board[x][y] == '1' or board[x+1][y+1] == '1':
            return False
        else:
            return True
    elif dir == 2:  # |
        if x - 1 < 0 or x + 1 >= N or y < 0 or y >= N:
            return False
        elif board[x-1][y] == '1' or board[x][y] == '1' or board[x+1][y] == '1':
            return False
        else:
            return True
    else:  # / or \
        if x - 1 < 0 or x + 1 >= N or y - 1 < 0 or y + 1 >= N:
            return False
        elif board[x-1][y+1] == '1' or board[x][y] == '1' or board[x+1][y-1] == '1':
            return False
        else:
            return True


N = int(input())
board = [list(input()) for _ in range(N)]
visit = [[[0]*4 for _ in range(N)] for _ in range(N)]

start_point = []
end_point = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'E':
            end_point.append([i, j])
        elif board[i][j] == 'B':
            start_point.append([i, j])

start_dir = get_dir(start_point)
end_dir = get_dir(end_point)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dq = deque([[start_point[1][0], start_point[1][1], start_dir]])
visit[start_point[1][0]][start_point[1][1]][start_dir] = 1  # x, y, dir
while dq:
    cur = dq.popleft()
    if cur[0] == end_point[1][0] and cur[1] == end_point[1][1] and cur[2] == end_dir:
        print(visit[cur[0]][cur[1]][cur[2]] - 1)
        exit()
    for i in range(4):
        nx, ny = cur[0] + dx[i], cur[1] + dy[i]
        if not check(nx, ny, cur[2]):
            continue
        if visit[nx][ny][cur[2]]:
            continue
        dq.append([nx, ny, cur[2]])
        visit[nx][ny][cur[2]] = visit[cur[0]][cur[1]][cur[2]] + 1
    if can_turn(cur[0], cur[1]):
        new_dir = (cur[2] + 2) % 4
        if not visit[cur[0]][cur[1]][new_dir]:
            dq.append([cur[0], cur[1], new_dir])
            visit[cur[0]][cur[1]][new_dir] = visit[cur[0]][cur[1]][cur[2]] + 1
print(0)
# print(dq, start_point, start_dir, end_point, end_dir)
