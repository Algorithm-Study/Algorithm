from collections import deque


def move_team():
    for idx in range(len(rail_road)):
        clock = team[idx][0]
        teammate = len(team[idx]) - 1
        start = 0
        for i in range(len(rail_road[idx])):
            if rail_road[idx][i][2] == 1:
                start = i
        if clock:
            dir = 1
        else:
            dir = -1
        tp = rail_road[idx][(start + dir + len(rail_road[idx])) % len(rail_road[idx])][2]
        for i in range(teammate):
            if clock:
                nx = (start - i + 1 + len(rail_road[idx])) % len(rail_road[idx])
                sx = (start - i + len(rail_road[idx])) % len(rail_road[idx])
                rail_road[idx][nx][2] = rail_road[idx][sx][2]
                team[idx][i+1] = rail_road[idx][nx]
            else:
                nx = (start + i - 1 + len(rail_road[idx])) % len(rail_road[idx])
                sx = (start + i + len(rail_road[idx])) % len(rail_road[idx])
                rail_road[idx][nx][2] = rail_road[idx][sx][2]
                team[idx][i+1] = rail_road[idx][nx]
            if i == teammate-1 and len(rail_road[idx]) == teammate:
                rail_road[idx][nx][2] = tp
        if len(rail_road[idx]) != teammate:
            rail_road[idx][(start + -dir * (teammate - 1) + len(rail_road[idx])) % len(rail_road[idx])][2] = tp

def setup_team():
    for rail in rail_road:
        temp = []
        start = 0
        clock = True
        for i in range(len(rail)):
            if rail[i][2] == 1:
                if rail[i-1][2] == 2:
                    start = i
                    clock = True
                else:
                    start = i
                    clock = False
                break
        temp.append(clock)
        while True:
            temp.append(rail[start])
            if rail[start][2] == 3:
                break
            if clock:
                start -= 1
                start = (start + len(rail)) % len(rail)
            else:
                start += 1
                start %= len(rail)
        team.append(temp)


def shoot_ball(round):
    point = 0
    if (round // n) % 4 == 0:
        # y 0 -> n-1
        x = round % n
        for y in range(n):
            for ti, tm in enumerate(team):
                for idx in range(1, len(tm)):
                    if tm[idx][0] == x and tm[idx][1] == y:
                        return idx * idx, ti
    elif (round // n) % 4 == 1:
        # x n-1 -> 0
        y = round % n
        for x in range(n-1, -1, -1):
            for ti, tm in enumerate(team):
                for idx in range(1, len(tm)):
                    if tm[idx][0] == x and tm[idx][1] == y:
                        return idx * idx, ti
    elif (round // n) % 4 == 2:
        # y n-1 -> 0
        x = round % n
        for y in range(n-1, -1, -1):
            for ti, tm in enumerate(team):
                for idx in range(1, len(tm)):
                    if tm[idx][0] == x and tm[idx][1] == y:
                        return idx * idx, ti
    else:
        # x 0 -> n-1
        y = round % n
        for x in range(n):
            for ti, tm in enumerate(team):
                for idx in range(1, len(tm)):
                    if tm[idx][0] == x and tm[idx][1] == y:
                        return idx * idx, ti
    return 0, -1


def change_head(tn):
    temp = team[tn][1:][::-1]
    temp[0][2] = 1
    temp[-1][2] = 3
    if team[tn][0]:
        clock = False
    else:
        clock = True
    new_temp = [clock] + temp
    team[tn] = new_temp



def dfs(cx, cy):
    # print("i", cx, cy)
    for di in range(4):
        nx = cx + dx[di]
        ny = cy + dy[di]
        # print(nx, ny)
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] == 0 or visit[nx][ny] > 0:
            continue
        visit[nx][ny] = 1
        temp.append([nx, ny, board[nx][ny]])
        dfs(nx, ny)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
rail_road = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] != 0 and visit[i][j] == 0:
            temp = deque()
            dfs(i, j)
            rail_road.append(temp)
team = deque()
setup_team()
ans = 0
for round in range(k):
    # print(round)
    # print(rail_road)
    # print(team)
    # print()
    move_team()
    # print(rail_road)
    # print(team)
    # print()
    point, tn = shoot_ball(round)
    ans += point
    if tn >= 0:
        change_head(tn)
        # print(rail_road)
        # print(team)
        # print()
print(ans)