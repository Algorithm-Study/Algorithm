def move_runner(seeker):
    temp = [[[] for j in range(n)] for i in range(n)]
    sx = seeker[0]
    sy = seeker[1]
    # print("sx", sx, sy)
    for i in range(n):
        for j in range(n):
            # 술래와의 거리가 3 이하인 도망자만 움직임
            if abs(sx - i) + abs(sy - j) <= 3:

                for di in hiders[i][j]:
                    # print(i, j, di, len(hiders[i][j]))
                    # 다음 좌표
                    nx = i + dx[di]
                    ny = j + dy[di]
                    # 격자를 벗어나면
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        # 방향을 반대로 틀어줌
                        if di % 2 == 1:
                            di -= 1
                        else:
                            di += 1
                        nx = i + dx[di]
                        ny = j + dy[di]
                    # 해당 위치에 술래가 없다면 이동
                    if not (nx == sx and ny == sy):
                        # print("nx", nx, ny, di)
                        temp[nx][ny].append(di)
                    else:
                        temp[i][j].append(di)

            else:
                for di in hiders[i][j]:
                    temp[i][j].append(di)
    return temp


def move_seeker_list(nx, ny):
    temp = []
    move_count = 0
    itr = 1
    dir = 0
    while True:
        move_count += 1
        for _ in range(itr):
            nx += mx[dir]
            ny += my[dir]
            if (nx, ny) == (-1, 0):
                return temp, itr
            temp.append([nx, ny, dir])
        dir = (dir + 5) % 4
        temp[-1][2] = dir
        if move_count == 2:
            move_count = 0
            itr += 1


def reverse_move_seeker_list(sx, sy, it):
    temp = []
    nx, ny = -1, 0
    dir = 2
    itr = it
    move_count = 0
    while True:
        for _ in range(itr-move_count):
            nx += mx[dir]
            ny += my[dir]
            if (nx, ny) == (sx, sy):
                temp.append([nx, ny, dir])
                return temp
            # print(nx, ny, dir)
            temp.append([nx, ny, dir])
        dir = (dir + 3) % 4
        temp[-1][2] = dir
        move_count += 1
        if move_count == 2:
            move_count = 0
            itr -= 1


def catch_runner(seeker):
    global hiders
    point = 0
    nx = seeker[0]
    ny = seeker[1]
    if len(hiders[nx][ny]) > 0 and not tree[nx][ny]:
        point += len(hiders[nx][ny])
        hiders[nx][ny] = []
    for i in range(2):
        nx += mx[seeker[2]]
        ny += my[seeker[2]]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            break
        if tree[nx][ny]:
            continue
        point += len(hiders[nx][ny])
        hiders[nx][ny] = []
        # print("hi", nx, ny, hiders[nx][ny])
    return point


mx = [-1, 0, 1, 0]
my = [0, 1, 0, -1]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m, h, k = map(int, input().split())
tree = [[False]*n for _ in range(n)]
hiders = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, d = map(int, input().split())
    hiders[x-1][y-1].append(d*2-1)
for _ in range(h):
    x, y = map(int, input().split())
    tree[x-1][y-1] = True
ans = 0
sx, sy = n//2, n//2
msl, itr = move_seeker_list(sx, sy)
msl[-1] = [0, 0, 2]
rmsl = reverse_move_seeker_list(sx, sy, itr)
rmsl.pop(0)
rmsl[-1] = [sx, sy, 0]
msl += rmsl
turn = 0
hiders = move_runner((sx, sy, 0))
for turn in range(k):
    # print(turn)

    # for i in range(n):
    #     print(hiders[i])
    # print()
    num = catch_runner(msl[turn % len(msl)])
    # print(turn % len(msl), msl[turn % len(msl)])
    # for i in range(n):
    #     print(hiders[i])
    # print()
    ans += num * (turn+1)
    hiders = move_runner(msl[turn % len(msl)])
print(ans)