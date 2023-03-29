# 변수 설정
r, c, t = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(r)]

answer = 0

# 공기 청정기 위치 탐색
for i in range(r):
    if maps[i][0] == -1:
        up = i
        down = i + 1
        break
    
# 미세먼지 확산
def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_maps = [[0] * c for _ in range(r)]
    
    # 확산 미세먼지 및 잔류 미세먼지 계산
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 0 and maps[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if nx >= 0 and nx < r and ny >= 0 and ny < c and maps[nx][ny] != -1:
                        tmp_maps[nx][ny] += maps[i][j] // 5
                        tmp += maps[i][j] // 5
                maps[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            maps[i][j] += tmp_maps[i][j]
            
# 위쪽 공기 반시계 방향 순환
def air_ccw():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        
        if x == up and y == 0:
            break
        
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        
        maps[x][y], before = before, maps[x][y]
        x = nx
        y = ny

# 아래쪽 공기 시계 방향 순환
def air_cw():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        
        if x == down and y == 0:
            break
        
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        
        maps[x][y], before = before, maps[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    air_ccw()
    air_cw()


print(sum(sum(maps,[2])))