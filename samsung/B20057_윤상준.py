# Python3 41440KB / 1888ms
# PyPy3 117820KB / 488ms
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dust_x = [[-1, 1, -1, 1, -1, 1, -2, 2, 0], [-1, -1, 0, 0, 1, 1, 0, 0, 2],
          [-1, 1, -1, 1, -1, 1, -2, 2, 0], [1, 1, 0, 0, -1, -1, 0, 0, -2]]
dust_y = [[1, 1, 0, 0, -1, -1, 0, 0, -2], [-1, 1, -1, 1, -1, 1, -2, 2, 0],
          [-1, -1, 0, 0, 1, 1, 0, 0, 2], [-1, 1, -1, 1, -1, 1, -2, 2, 0]]
dust_ratio = [1, 1, 7, 7, 10, 10, 2, 2, 5]
x, y = N//2, N//2
move = 0
oof_dust = 0
while True:
    for i in range(4):
        if i == 2 or i == 0:
            move += 1
        # 먼지 이동 계산
        for _ in range(move):
            x, y = x + dx[i], y + dy[i]
            dust_lost = 0
            if x < 0 or y < 0 or x >= N or y >= N:
                print(oof_dust)
                exit()
            for nx, ny, ratio in zip(dust_x[i], dust_y[i], dust_ratio):
                d_x, d_y = x + nx, y + ny
                #print(dust_x, dust_y)
                if d_x < 0 or d_y < 0 or d_x >= N or d_y >= N:
                    oof_dust += (field[x][y] * ratio) // 100
                else:
                    field[d_x][d_y] += (field[x][y] * ratio) // 100
                dust_lost += (field[x][y] * ratio) // 100
            #print(dust_lost)
            move_x, move_y = x + dx[i], y + dy[i]
            if move_x < 0 or move_y < 0 or move_x >= N or move_y >= N:
                oof_dust += field[x][y] - dust_lost
            else:
                field[move_x][move_y] += field[x][y] - dust_lost
            field[x][y] = 0

