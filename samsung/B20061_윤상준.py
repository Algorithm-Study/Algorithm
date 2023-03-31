# 한 줄이 모두 채워진 경우에 한 칸 씩 내려가는 과정에 대한 조건을 잘 구현해야 함!
# python3 메모리: 31972 시간: 932
# pypy3 메모리: 131012 시간: 620ms
# https://sogogi1000inbun.tistory.com/33 
from copy import deepcopy
n = int(input())
blue = [[0 for _ in range(4)] for _ in range(6)]
green = [[0 for _ in range(4)] for _ in range(6)]
blue_level = [0]*4
blue_bingo = [0]*6
green_level = [0]*4
green_bingo = [0]*6
total_score = 0
for _ in range(n):
    block, x, y = map(int, input().split())
    # 1x1 블록인 경우
    if block == 1:
        blue[blue_level[x]][x] = 1
        blue_bingo[blue_level[x]] +=1
        blue_level[x] += 1
        green[green_level[y]][y] = 1
        green_bingo[green_level[y]] +=1
        green_level[y] += 1
    # 1X2 블록인 경우
    elif block == 2:
        blue[blue_level[x]][x] = 1
        blue[blue_level[x] + 1][x] = 1
        blue_bingo[blue_level[x]] +=1
        blue_bingo[blue_level[x] + 1] +=1
        blue_level[x] += 2
        level = max(green_level[y], green_level[y+1])
        green[level][y] = 1
        green[level][y+1] = 1
        green_level[y] = level + 1
        green_level[y + 1] = level + 1
        green_bingo[level] += 2
    # 2X1 블록인 경우
    elif block == 3:
        level = max(blue_level[x], blue_level[x+1])
        blue[level][x] = 1
        blue[level][x+1] = 1
        blue_level[x] = level + 1
        blue_level[x + 1] = level + 1
        blue_bingo[level] += 2
        green[green_level[y]][y] = 1
        green[green_level[y] + 1][y] = 1
        green_bingo[green_level[y]] +=1
        green_bingo[green_level[y] + 1] +=1
        green_level[y] += 2
    ####디버깅용 출력 ####
    #for i in range(5,-1,-1):
    #   print(green[i])
    # bingo 있는 경우
    while 4 in green_bingo:
        total_score += 1
        bingo = green_bingo.index(4)
        for i in range(bingo+1, 6):
            green[i-1] = deepcopy(green[i])
            green_bingo[i-1] = green_bingo[i]
        green[5] = [0,0,0,0]
        green_bingo[5] = 0
        for i in range(4):
            green_level[i] = 0
            for j in range(5, -1, -1):
                if green[j][i] == 1:
                    green_level[i] = j+ 1
                    break
    while 4 in blue_bingo:
        total_score += 1
        bingo = blue_bingo.index(4)
        for i in range(bingo+1, 6):
            blue[i-1] = deepcopy(blue[i])
            blue_bingo[i-1] = blue_bingo[i]
        blue[5] = [0,0,0,0]
        blue_bingo[5] = 0
        for i in range(4):
            blue_level[i]=0
            for j in range(5, -1, -1):
                if blue[j][i] == 1:
                    blue_level[i] = j+ 1
                    break
    # 넘친 경우
    while sum([x>=5 for x in blue_level]):
        for i in range(1,6):
            blue[i-1] = deepcopy(blue[i])
            blue_bingo[i-1] = blue_bingo[i]
        blue[5] = [0,0,0,0]
        blue_bingo[5] = 0
        for i in range(4):
            if blue_level[i] != 0:
                blue_level[i] -= 1
    while sum([x>=5 for x in green_level]):
        for i in range(1,6):
            green[i-1] = deepcopy(green[i])
            green_bingo[i-1] = green_bingo[i]
        green[5] = [0,0,0,0]
        green_bingo[5] = 0
        for i in range(4):
            if green_level[i] != 0:
                green_level[i] -= 1
print(total_score)
green_block = sum(map(sum, green))
blue_block = sum(map(sum, blue))
print(green_block + blue_block)           