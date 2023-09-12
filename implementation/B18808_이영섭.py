def rotate90(idx):
    global sticker
    i = len(sticker[idx])
    j = len(sticker[idx][0])
    new_list = [[0]*i for _ in range(j)]
    for x in range(j):
        for y in range(i):
            new_list[x][y] = sticker[idx][i-1-y][x]
            # 0 0 = 1 0
            # 0 1 = 0 0
            # 4 0 = 1 4
            # 4 1 = 0 4
    sticker[idx] = new_list


def find_point(idx):
    if n - len(sticker[idx]) < 0 or m - len(sticker[idx][0]) < 0:
        return False
    for sx in range(n - len(sticker[idx]) + 1):
        for sy in range(m - len(sticker[idx][0]) + 1):
            # 스티커
            if fit(sx, sy, idx):
                change_board(sx, sy, idx)
                return True
    return False


def fit(sx, sy, idx):
    for i in range(len(sticker[idx])):
        for j in range(len(sticker[idx][0])):
            if board[sx + i][sy + j] == 1 and sticker[idx][i][j] == 1:
                return False
    return True


def change_board(sx, sy, idx):
    for i in range(len(sticker[idx])):
        for j in range(len(sticker[idx][0])):
            if sticker[idx][i][j] == 1:
                board[sx + i][sy + j] = 1


n, m, k = map(int, input().split())
sticker = []
board = [[0]*m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    sticker.append([list(map(int, input().split())) for _ in range(r)])

for idx, s in enumerate(sticker):
    for _ in range(4):
        if find_point(idx):
            break
        else:
            rotate90(idx)

ans = 0
for i in range(n):
    ans += sum(board[i])
print(ans)
