dx = [-1 ,1, 0, 0]
dy = [0, 0, -1, 1]
# n X n, m마리, 냄새 지속 기간:k
n,m,K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
# 상어가 격자 안에 있는지 여부
shark_status = [1]*(m+1)
shark_status[0] = 0
# 위 아래 왼쪽 오른쪽
shark_current = [-1] + [x-1 for x in list(map(int, input().split()))]
shark_move = []
for _ in range(m):
    temp = []
    for _ in range(4):
        line = list(map(int, input().split()))
        temp.append(line)
    shark_move.append(temp)
# smell -> [time,shark_num]
smell = [[[0,0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in  range(n):
        if field[i][j] != 0:
            smell[i][j] = [K,field[i][j]]
time = 0
# 상어 이동 시작
while time <= 1000:
    # 1번 상어만 남은 경우 
    if sum(shark_status) == 1:
        break
    # 상어가 존재하는 지 체크하면서 이동
    new_field = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if field[i][j] != 0:
                shark_num = field[i][j]
                moving_list = []
                priority = shark_move[shark_num-1][shark_current[shark_num]]
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    # 범위 밖으로 벗어난 경우
                    if nx < 0 or ny < 0 or nx >= n or ny >=n:
                        continue
                    # 냄새가 없는 공간인 경우(공백 여부, 우선순위, 위치, 방향)
                    if smell[nx][ny] == [0,0]:
                        moving_list.append((0,priority.index(k+1), nx, ny, k))
                    # 자신의 냄새가 있는 공간인 경우
                    elif smell[nx][ny][1] == shark_num:
                        moving_list.append((1,priority.index(k+1), nx, ny, k))
                moving_list.sort(key = lambda x: (x[0],x[1]))
                _, _, nx,ny,way = moving_list[0]
                # 상어 이동 후 겹치는 상어가 있는 경우 처리
                if new_field[nx][ny] != 0:
                    # 더 강한 상어가 있는 경우
                    if new_field[nx][ny] < shark_num:
                        shark_status[shark_num] = 0
                    # 자신이 더 강한 상어인 경우
                    else:
                        #이전 상어 맵에서 제거
                        shark_status[new_field[nx][ny]] = 0
                        #현재 상어로 대체
                        new_field[nx][ny] = shark_num
                        shark_current[shark_num] = way
                # 빈 자리인 경우
                else:
                    new_field[nx][ny] = shark_num
                    shark_current[shark_num] = way
    # 냄새 갱신
    for i in range(n):
        for j in range(n):
            # 냄새 정보가 있는 경우
            if smell[i][j] != [0,0]:
                duration, shark_num = smell[i][j]
                duration -= 1
                # 냄새 지속 시간이 끝난 경우 제거
                if duration == 0:
                    smell[i][j] = [0,0]
                else:
                    smell[i][j] = [duration,shark_num]
    # 맵 갱신 및 냄새 정보 갱신
    field = [x[:] for x in new_field]
    for i in range(n):
        for j in range(n):
            if field[i][j] != 0:
                smell[i][j] = [K, field[i][j]]
    time += 1
if sum(shark_status) == 1 and time <= 1000:
    print(time)
else:
    print(-1)
# 방향 우선 순위에 대해서 잘 이해하고 문제 풀 것!