from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def out_board(nx, ny):
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        return True
    return False


def move(x, y, d, s, num, gun):
    nx, ny = x + dx[d], y + dy[d]
    if out_board(nx, ny):
        d = (d + 2) % 4
        nx, ny = x + dx[d], y + dy[d]
    return nx, ny, d, s, num, gun


def change_gun(num, x, y):
    global board
    if len(board[x][y]):
        gun = max(board[x][y])
    else:
        return player[num][5]
    if player[num][5] < gun:
        idx = board[x][y].index(gun)
        board[x][y][idx] = player[num][5]
        return gun
    return player[num][5]


def fight(op, np, nx, ny):
    global player
    # 기존에 있던 player 번호와 새로 온 친구 번호
    # 둘의 s + gun을 비교해서
    # 이긴 친구의 번호와, 점수를 return
    if player[op][3] + player[op][5] > player[np][3] + player[np][5]:
        # 총 버리기
        point = (player[op][3] + player[op][5]) - (player[np][3] + player[np][5])
        board[nx][ny].append(player[np][5])
        player[np][5] = 0
        return op, np, point
    elif player[op][3] + player[op][5] < player[np][3] + player[np][5]:
        point = (player[np][3] + player[np][5]) - (player[op][3] + player[op][5])
        board[nx][ny].append(player[op][5])
        player[op][5] = 0
        return np, op, point
    else:
        if player[op][3] > player[np][3]:
            board[nx][ny].append(player[np][5])
            player[np][5] = 0
            return op, np, 0
        else:
            board[nx][ny].append(player[op][5])
            player[op][5] = 0
            return np, op, 0


def loser_move(num):
    global player
    x, y, di = player[num][0], player[num][1], player[num][2]
    nx, ny = x + dx[di], y + dy[di]
    while out_board(nx, ny) or player_board[nx][ny] > 0:
        di = (di + 5) % 4
        nx, ny = x + dx[di], y + dy[di]
    return nx, ny, di


n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
player_board = [[0] * n for _ in range(n)]
for i in range(n):
    gun = list(map(int, input().split()))
    for j in range(n):
        if gun[j] > 0:
            board[i][j].append(gun[j])
player = []
for i in range(m):
    x, y, d, s = map(int, input().split())
    player.append([x-1, y-1, d, s, i, 0])
    player_board[x-1][y-1] = i+1
ans = [0] * m
for turn in range(k):
    # print('turn', turn)
    for p in player:
        nx, ny, d, s, num, gun = move(p[0], p[1], p[2], p[3], p[4], p[5])  # 이동만
        # print('num', num)
        if player_board[nx][ny] > 0:
            player_board[p[0]][p[1]] = 0
            player[num] = [nx, ny, d, s, num, gun]
            # print(nx, ny, player_board[nx][ny])
            vic, defeat, point = fight(player_board[nx][ny]-1, num, nx, ny)  # 진 사람은 총 내려놓고 이긴 사람은 총 바꾸기까지
            # print(vic, defeat)
            ans[vic] += point
            gun = change_gun(vic, nx, ny)
            player[vic][5] = gun
            lx, ly, di = loser_move(defeat)  # 이동만
            # print(lx, ly)
            gun = change_gun(defeat, lx, ly)
            player[defeat][0], player[defeat][1], player[defeat][2], player[defeat][5] = lx, ly, di, gun
            player_board[nx][ny], player_board[lx][ly] = player[vic][4]+1, player[defeat][4]+1
        else:
            player_board[nx][ny], player_board[p[0]][p[1]] = num+1, 0
            gun = change_gun(num, nx, ny)
            player[num] = [nx, ny, d, s, num, gun]
        # print("player")
        # print(player)
        # print("player board")
        # for i in range(n):
        #     print(player_board[i])
        # print("board")
        # for i in range(n):
        #     print(board[i])
        # print("ans")
        # for a in ans:
        #     print(a, end=" ")
        # print()

for a in ans:
    print(a, end=" ")