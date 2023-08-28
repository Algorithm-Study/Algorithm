n, m, k = map(int, input().split())

# 초기 상어 위치
position = []
for _ in range(n):
    position.append(list(map(int, input().split())))

# 초기 상어 방향
direcions = list(map(int, input().split()))

# 상어 방향 우선순위
priority = []
for _ in range(m):
    tmp = []
    for _ in range(4):
        tmp.append(list(map(int, input().split())))
    priority.append(tmp)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 냄새 정보
smell = [[[0, 0]]*n for _ in range(n)]

# 냄새 정보 갱신
def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
                
            if position[i][j] != 0:
                smell[i][j] = [position[i][j], k]
                
# 상어 이동     
def move_shark():
    tmp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if position[x][y] != 0:
                d = direcions[position[x][y] - 1]
                found = False
                
                # 상어의 위치인 경우
                for idx in priority[position[x][y]-1][d-1]:
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        
                        # 냄새가 없는 곳이면
                        if smell[nx][ny][1] == 0:
                            direcions[position[x][y]-1] = idx
                            
                            # 상어 이동
                            if tmp[nx][ny] == 0:
                                tmp[nx][ny] = position[x][y]
                            else:
                                tmp[nx][ny] = min(position[x][y], tmp[nx][ny])
                            found = True
                            break
                if found:
                    continue
                
                # 주변이 모두 냄새가 있다면, 자신의 냄새로 이동
                for idx in priority[position[x][y]-1][d-1]:
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        
                        # 자신의 냄새가 있는 곳이면 방향 변경 및 이동
                        if smell[nx][ny][0] == position[x][y]:
                            direcions[position[x][y]-1] = idx
                            tmp[nx][ny] = position[x][y]
                            break
    return tmp

answer = 0
while True:
    update_smell()
    position = move_shark()
    answer += 1
    
    check = True
    for i in range(n):
        for j in range(n):
            if position[i][j] > 1:
                check = False
                
    if check:
        print(answer)
        break
    
    if answer >= 1000:
        print(-1)
        break