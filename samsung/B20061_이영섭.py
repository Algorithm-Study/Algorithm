N = int(input())
board = [[0 for _ in range(10)] for _ in range(10)]
dx = [1, 0]
dy = [0, 1]
ans, cnt = 0, 0

def move(t, x, y):
    if t == 1:
        tx, ty = x, y
        for i in range(9-x):
            if board[tx+1][y] == 1 or tx+1 == 10:
                break
            tx += 1
        for j in range(9-y):
            if board[x][ty+1] == 1 or ty+1 == 10:
                break
            ty += 1
        board[tx][y] = 1
        board[x][ty] = 1
            
    if t == 2:
        tx, ty = x, y+1
        for i in range(9-tx):
            if board[tx+1][y] == 1 or board[tx+1][y+1] == 1 or tx+1 == 10:
                break
            tx += 1
        for j in range(9-ty):
            if board[x][ty+1] == 1 or ty+1 == 10:
                break
            ty += 1
        board[tx][y] = 1
        board[tx][y+1] = 1
        board[x][ty] = 1
        board[x][ty-1] = 1
    elif t == 3:
        tx, ty = x+1, y
        for i in range(9-tx):
            if board[tx+1][y] == 1 or tx+1 == 10:
                break
            tx += 1
        for j in range(9-ty):
            if board[x][ty+1] == 1 or board[x+1][ty+1] == 1 or ty+1 == 10:
                break
            ty += 1
        board[tx][y] = 1
        board[tx-1][y] = 1
        board[x][ty] = 1
        board[x+1][ty] = 1

def check():
    tpx, tpy = [], []
    tempx, tempy = [], []
    for i in range(9, 5, -1):
        cntx = 0
        cnty = 0
        for j in range(4):
            if board[i][j] == 1:
                cntx += 1
            if board[j][i] == 1:
                cnty += 1
        if cntx == 4:
            tpx.append(i)
        if cnty == 4:
            tpy.append(i)
            
    if tpx : tempx = [x for x in [9, 8, 7, 6] if x not in tpx]
    if tpy : tempy = [y for y in [9, 8, 7, 6] if y not in tpy]
    for i in range(len(tempx)):
        for j in range(4):
            board[9-i][j] = board[tempx[i]][j]
    for i in range(len(tpx)):
        for j in range(4):
            board[6+i][j] = 0
    for i in range(len(tempy)):
        for j in range(4):
            board[j][9-i] = board[j][tempy[i]]
    for i in range(len(tpy)):
        for j in range(4):
            board[j][6+i] = 0
    for i in range(2):
        for j in range(4):
            board[5+len(tpx)-i][j] = board[5-i][j]
            board[j][5+len(tpy)-i] = board[j][5-i]
    return len(tpx) + len(tpy)

def green():
    tempx, tempy = 0, 0
    for i in range(5, 3, -1):
        for j in range(4):
            if board[i][j] == 1:
                tempx += 1
                break
    for i in range(5, 3, -1):
        for j in range(4):
            if board[j][i] == 1:
                tempy += 1
                break
    if tempx > 0:
        for i in range(9, 5, -1):
            for j in range(4):
                board[i][j] = board[i-tempx][j]
    if tempy > 0:
        for i in range(9, 5, -1):
            for j in range(4):
                board[j][i] = board[j][i-tempy]
    for i in range(tempx):
        for j in range(4):
            board[5-i][j] = 0
    for i in range(tempy):
        for j in range(4):
            board[j][5-i] = 0

for _ in range(N):
    t, x, y = map(int, input().split())
    move(t, x, y)
    # print()
    # for i in range(10):
    #     print(board[i])
    ans += check()
    # print()
    # for i in range(10):
    #     print(board[i])
    green()
    # print()
    # for i in range(10):
    #     print(board[i])

for i in range(6, 10):
    for j in range(4):
        if board[i][j] == 1:
            cnt += 1
        if board[j][i] == 1:
            cnt += 1

print(ans)
print(cnt)

# 블록이 주어지면 초록색과 파란색의 끝으로 보냄
# 초록색의 행과 파란색의 열을 검사하며 올라옴
# 사라진 줄만큼 점수를 획득하고 블록들을 끝으로 보냄
# 줄이 사라지지 않고 초록색 줄에 남으면 초록색 줄의 개수만큼 각각 아래 블록을 삭제