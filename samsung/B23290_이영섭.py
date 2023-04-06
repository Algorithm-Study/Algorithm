def copy_magic():
    # 복제 시전 -> temp
    copy_fish = []
    for i in range(4):
        for j in range(4):
            for k in range(1, 9):
                if fish[i][j][k] > 0:
                    copy_fish.append((i, j, k, fish[i][j][k]))
    return copy_fish


def move_fish():
    # 물고기 이동
    # 상어가 있는 칸 x
    # 물고기의 냄새가 있는 칸 x
    # 격자의 범위를 벗어나는 칸 x
    # 셋다 안되면 45도 반시계 회전
    temp = [[[0]*9 for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            if fish[i][j][0] == 1:
                temp[i][j][0] = 1
            for k in range(1, 9):
                if fish[i][j][k] > 0:
                    # print(i, j, k)
                    dir = k
                    for _ in range(8):
                        nx = i + dx[dir]
                        ny = j + dy[dir]
                        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or smell[nx][ny] > 0 or fish[nx][ny][0] == 1:
                            if dir == 1:
                                dir = 8
                            else:
                                dir -= 1
                        else:
                            temp[nx][ny][dir] += fish[i][j][k]
                            # print("nx", nx, ny, dir)
                            break
                    else:
                        temp[i][j][k] = fish[i][j][k]
    return temp


def product(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr, r-1):
                yield [arr[i]] + next


def move_shark(sx, sy, time):
    # 상어가 연속해서 3칸 이동
    # 격자를 벗어나면 x
    # 제외되는 물고기의 수가 가장 많은 방법으로
    # 물고기가 있는 칸에 가면 물고기 -> 물고기 냄새
    max_eat = -1
    route = []
    # print(bf)
    for case in bf:
        nx = sx
        ny = sy
        eat_fish = 0
        temp = [[fish[i][j][:] for j in range(4)] for i in range(4)]
        # print(case)
        for dir in case:
            nx += mx[dir]
            ny += my[dir]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                break
            eat_fish += sum(temp[nx][ny])
            temp[nx][ny] = [0] * 9
            # print(f"dir: {dir}, nx: {nx}, ny: {ny}, val: {fish[nx][ny]}")
        else:
            if eat_fish > max_eat:
                max_eat = eat_fish
                route = case
    print(route)
    for dir in route:
        sx += mx[dir]
        sy += my[dir]
        cnt = 0
        for k in range(1, 9):
            if fish[sx][sy][k]:
                fish[sx][sy][k] = 0
                cnt += 1
        if cnt:
            smell[sx][sy] = time
    return sx, sy


def remove_smell(time):
    for i in range(4):
        for j in range(4):
            if smell[i][j] == 0:
                continue
            if time - smell[i][j] == 2:
                smell[i][j] = 0


dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
mx = [0, -1, 0, 1, 0]
my = [0, 0, -1, 0, 1]
M, S = map(int, input().split())
fish = [[[0]*9 for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]
for i in range(M):
    fx, fy, d = map(int, input().split())
    fish[fx-1][fy-1][d] += 1
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
fish[sx][sy][0] = 1
bf = list(product([1, 2, 3, 4], 3))

for time in range(1, S+1):
    temp = copy_magic()
    fish = move_fish()
    for i in range(4):
        print(fish[i])
    print()
    fish[sx][sy][0] = 0
    sx, sy = move_shark(sx, sy, time)
    fish[sx][sy][0] = 1
    for i in range(4):
        print(smell[i])
    print()
    remove_smell(time)
    for tp in temp:
        fish[tp[0]][tp[1]][tp[2]] += tp[3]
    for i in range(4):
        print(fish[i])
    print()
    for i in range(4):
        print(smell[i])
    print()


ans = 0
for i in range(4):
    for j in range(4):
        for k in range(1, 9):
            ans += fish[i][j][k]
print(ans)
