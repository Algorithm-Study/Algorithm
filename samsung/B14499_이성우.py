N, M, x0, y0, orders = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]
orders_list = list(map(int, input().split()))

# print('-'*2*M)
# for _ in maps:
#     print(*_)
    
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
        
nx, ny = x0, y0
for i in orders_list:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[-1]
    else:
        dice[-1] = maps[nx][ny]
        maps[nx][ny] = 0

    print(dice[0])

    