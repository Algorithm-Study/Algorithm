from collections import deque


def heat_wind(dir, x, y):
    global wind
    temp = [[0]*C for _ in range(R)]
    if dir == 1:
        for idx, j in enumerate(range(1, 6)):
            for i in range(-j+1, j):
                nx, ny = x + i, y + j
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if idx == 0:
                    temp[nx][ny] = 5
                # 왼 오 아 위
                for num, cx, cy in [(2, 0, 1), (3, -1, 1), (4, 1, 1)]:
                    if new_board[nx][ny][num] == 1:
                        continue
                    sx = nx + cx
                    sy = ny + cy
                    if sx < 0 or sy < 0 or sx >= R or sy >= C:
                        continue
                    if new_board[sx][sy][dir] == 1 or temp[sx][sy] != 0:
                        continue
                    temp[sx][sy] = 4 - idx
    elif dir == 2:
        for idx, j in enumerate(range(-1, -6, -1)):
            for i in range(j+1, -j):
                nx, ny = x + i, y + j
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if idx == 0:
                    temp[nx][ny] = 5
                # 왼 오 아 위
                for num, cx, cy in [(1, 0, -1), (3, 1, -1), (4, -1, -1)]:
                    if new_board[nx][ny][num] == 1:
                        continue
                    sx = nx + cx
                    sy = ny + cy
                    if sx < 0 or sy < 0 or sx >= R or sy >= C:
                        continue
                    if new_board[sx][sy][dir] == 1 or temp[sx][sy] != 0:
                        continue
                    temp[sx][sy] = 4 - idx
    elif dir == 3:
        for idx, i in enumerate(range(-1, -6, -1)):
            for j in range(i+1, -i):
                nx, ny = x + i, y + j
                # print(nx, ny, end=" ")
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if idx == 0:
                    temp[nx][ny] = 5
                # 왼 오 아 위
                for num, cx, cy in [(1, -1, -1), (2, -1, 1), (4, -1, 0)]:
                    if new_board[nx][ny][num] == 1:
                        continue
                    sx = nx + cx
                    sy = ny + cy
                    if sx < 0 or sy < 0 or sx >= R or sy >= C:
                        continue
                    if new_board[sx][sy][dir] == 1 or temp[sx][sy] != 0:
                        continue
                    temp[sx][sy] = 4 - idx
    elif dir == 4:
        for idx, i in enumerate(range(1, 6)):
            for j in range(-i+1, i):
                nx, ny = x + i, y + j
                print(nx, ny, end=" ")
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if idx == 0:
                    temp[nx][ny] = 5
                # 왼 오 아 위
                for num, cx, cy in [(1, 1, -1), (2, 1, 1), (3, 1, 0)]:
                    if new_board[nx][ny][num] == 1:
                        continue
                    sx = nx + cx
                    sy = ny + cy
                    if sx < 0 or sy < 0 or sx >= R or sy >= C:
                        continue
                    if new_board[sx][sy][dir] == 1 or temp[sx][sy] != 0:
                        continue
                    temp[sx][sy] = 4 - idx
    for i in range(R):
        for j in range(C):
            wind[i][j] += temp[i][j]


def manage_temp():
    global wind
    temp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            for k in range(1, 5):
                if new_board[i][j][k] != 0:
                    continue
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if wind[i][j] > wind[nx][ny]:
                    temp[i][j] -= (wind[i][j] - wind[nx][ny]) // 4
                    temp[nx][ny] += (wind[i][j] - wind[nx][ny]) // 4

    for i in range(R):
        for j in range(C):
            wind[i][j] += temp[i][j]
    for i in range(R):
        print(wind[i])
    print()
    for i in range(C):
        if wind[0][i]:
            wind[0][i] -= 1
        if wind[R-1][i]:
            wind[R-1][i] -= 1
    for i in range(1, R-1):
        if wind[i][0]:
            wind[i][0] -= 1
        if wind[i][C-1]:
            wind[i][C-1] -= 1
    for i in range(R):
        print(wind[i])
    print()


def check():
    for cl in cell:
        if wind[cl[0]][cl[1]] < K:
            return False
    else:
        return True


dx = [0, 0, 0, 1, -1]
dy = [0, -1, 1, 0, 0]
R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
airc, cell, cho = [], [], 0
new_board = [[[0, 0, 0, 0, 0]]*C for _ in range(R)]
wind = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        new_board[i][j] = [board[i][j], 0, 0, 0, 0]
        if board[i][j] == 5:
            cell.append((i, j))
        elif board[i][j] != 0:
            airc.append((board[i][j], i, j))
W = int(input())
wall = [list(map(int, input().split())) for _ in range(W)]
print(cell)
for wl in wall:
    if wl[2] == 0:  # 왼 오 아 위
        new_board[wl[0]-1][wl[1]-1][4] = 1
        if 0 <= wl[0]-2 < R:
            new_board[wl[0]-2][wl[1]-1][3] = 1
    else:
        new_board[wl[0]-1][wl[1]-1][2] = 1
        if 0 <= wl[1] < C:
            new_board[wl[0]-1][wl[1]][1] = 1
print(airc)
# for air in airc:
#     heat_wind(air[0], air[1], air[2])
# manage_temp()
# for i in range(R):
#     print(wind[i])
# print()
while True:
    # 온풍기 바람 나옴
    for air in airc:
        heat_wind(air[0], air[1], air[2])
    for i in range(R):
        print(wind[i])
    print()
    # 온도 조절
    manage_temp()
    # 초콜릿 먹기
    cho += 1
    if cho > 100:
        break
    # 온도 조사
    if check():
        break
if cho > 100:
    print(101)
else:
    print(cho)