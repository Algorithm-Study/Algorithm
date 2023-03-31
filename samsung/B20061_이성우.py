# 환경 설정
n = int(input())
blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]
score = 0

# 블루 타일 배치
def drop_blue(t, x):
    y =0
    if t in [1, 2]:
        for i in range(6):
            if blue[x][i] == 1:
                break
            y += 1
        y -= 1
        if t == 2:
            blue[x][y-1] = 1
        blue[x][y] = 1
    else:
        for i in range(6):
            if blue[x][i] == 1 or blue[x+1][i] == 1:
                break
            y += 1
        y -= 1
        blue[x][y], blue[x+1][y] = 1, 1

# 그린 타일 배치
def drop_green(t, y):
    x = 0
    if t in [1,3]:
        for i in range(6):
            if green[i][y] == 1:
                break
            x += 1
        x -= 1
        if t == 3:
            green[x-1][y] = 1
        green[x][y] = 1
    else:
        for i in range(6):
            if green[i][y] == 1 or green[i][y+1] == 1:
                break
            x += 1
        x -= 1
        green[x][y], green[x][y+1] = 1, 1

# 모두 배치된 타일 삭제
def delete(c, idx):
    # 삭제할 타일이 블루
    if c == 'b':
        # 삭제할 타일은 삭제하고 나머지는 당기기
        for i in range(idx, -1, -1):
            if i == 0:
                for j in range(4):
                    blue[j][i] = 0
            else:
                for j in range(4):
                    blue[j][i] = blue[j][i-1]
    # 삭제할 타일이 그린
    elif c == 'g':
        # 삭제할 타일은 삭제하고 나머지는 당기기
        for i in range(idx, -1, -1):
            if i == 0:
                for j in range(4):
                    green[i][j] = 0
            else:
                for j in range(4):
                    green[i][j] = green[i-1][j]

for _ in range(n):
    t, x, y = map(int, input().split())
    # 배치
    drop_blue(t, x)
    drop_green(t, y)

    # 삭제할 타일 탐색 후 점수 획득
    for i in range(6):
        b_cnt = 0
        for j in range(4):
            if blue[j][i] == 1:
                b_cnt += 1
        if b_cnt == 4:
            delete('b', i)
            score += 1
    for i in range(6):
        g_cnt = 0
        for j in range(4):
            if green[i][j] == 1:
                g_cnt += 1
        if g_cnt == 4:
            delete('g', i)
            score += 1
            
    # 밑으로 내릴 블루 타일 탐색
    for i in range(2):
        for j in range(4):
            if blue[j][i] == 1:
                delete('b', 5)
                break
    # 밑으로 내릴 그린 타일 탐색
    for i in range(2):
        for j in range(4):
            if green[i][j] == 1:
                delete('g', 5)
                break

# 타일 갯수 탐색
count = 0
for i in range(4):
    for j in range(6):
        if blue[i][j] == 1:
            count += 1
        if green[j][i] == 1:
            count += 1

print(score)
print(count)