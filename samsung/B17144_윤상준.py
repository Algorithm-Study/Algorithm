from copy import deepcopy
import sys
input = sys.stdin.readline
R, C, T = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
machine = []
# 공기청정기 위치 확인
for i in range(R):
    if field[i][0] == -1:
        machine.append(i)
for _ in range(T):
    temp = deepcopy(field)
    #먼저 퍼지게 만들기
    for i in range(R):
        for j in range(C):
            dust_go = 0
            dust_come = 0
            if field[i][j] == -1:
                 continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >=R or ny >=C or field[nx][ny] == -1:
                    continue
                dust_go += 1
                dust_come += field[nx][ny]//5
            temp[i][j] = field[i][j] - (field[i][j]//5 * dust_go) + dust_come
    field = deepcopy(temp)
    # 공기 정화
    # 상단부
    top = machine[0]
    for i in range(top-1,0,-1):
        field[i][0] = field[i-1][0]
    for i in range(0,C-1):
        field[0][i] = field[0][i+1]
    for i in range(0,top):
        field[i][C-1] = field[i+1][C-1]
    for i in range(C-1,1,-1):
        field[top][i] = field[top][i-1]
    field[top][1] = 0
    #하단부
    down = machine[1]
    for i in range(down+1,R-1):
        field[i][0] = field[i+1][0]
    for i in range(0,C-1):
        field[R-1][i] = field[R-1][i+1]
    for i in range(R-1,down,-1):
        field[i][C-1] = field[i-1][C-1]
    for i in range(C-1,1,-1):
        field[down][i] = field[down][i-1]
    field[down][1] = 0
total_dust = sum(map(sum, field))
#for i in range(R):
#    print(field[i])
print(total_dust + 2)              
        