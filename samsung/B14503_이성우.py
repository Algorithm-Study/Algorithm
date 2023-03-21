N, M = map(int, input().split())
x, y, idx = map(int, input().split())
if idx == 1:
    idx = 3
elif idx == 3:
    idx = 1
directions = [[-1,0],[0,-1],[1,0],[0,1]]
direction = directions[idx]
operation = True
maps = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

# 보는 방향 반시계로 회전
def rotate_direction(direction):
    idx = directions.index(direction)
    return directions[(idx+1)%4]

# 지문대로 주변 탐색
def check_around(maps, x, y, direction, operation):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    # 주변 4칸 중 청소 안된 곳이 있다면 break
    for i in range(4):
        if x+dx[i] < 0 or x+dx[i] >= N or y+dy[i] < 0 or y+dy[i] >= M:
            continue
        if maps[x+dx[i]][y+dy[i]] == 0:
            break
        
    # 주변 4칸이 청소가 모두 되었다면 보는 방향에서 뒤로 가고 못가면 작동 정지
    else:
        if x-direction[0] >= 0 and x-direction[0] < N and y-direction[1] >= 0 and y-direction[1] < M and maps[x-direction[0]][y-direction[1]] != 1:
                return maps, x-direction[0], y-direction[1], direction, operation
        else:
            operation = False
            return maps, x, y, direction, operation
            
    # 주변 4칸 중 청소 안된 곳이 있다면 반시계로 돌면서 탐지하고 청소 안된 곳으로 직진
    for _ in range(4):
        direction = rotate_direction(direction)
        if x+direction[0] < 0 or x+direction[0] >= N or y+direction[1] < 0 or y+direction[1] >= M:
            continue
        if maps[x+direction[0]][y+direction[1]] == 0:
            x = x+direction[0]
            y = y+direction[1]
            return maps, x, y, direction, operation    
    
# 로봇 청소 안되어 있으면 청소하고 주변 탐색
def robot(maps, x, y, direction, operation, cnt):
    if maps[x][y] == 0:
        cnt += 1
        maps[x][y] = 2

    return *check_around(maps, x, y, direction, operation), cnt

# 작동이 멈출 때까지 탐색
while operation:
    # print(maps, x, y, direction, operation, cnt)
    print(maps)
    maps, x, y, direction, operation, cnt = robot(maps, x, y, direction, operation, cnt)

# 청소한 영역 print
print(cnt)