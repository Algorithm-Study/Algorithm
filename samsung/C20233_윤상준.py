#n: 미로의 크기, m: 참가자 수, k: 게임시간
n,m,k = map(int, input().split())
# 초기 상태 입력(1,1 부터 시작이므로 하나 더 크게 생성)
field = [[0]*(n+1)] + [[0]+ list(map(int, input().split())) for _ in range(n)]
participants = [tuple(map(int, input().split())) for _ in range(m)]
goal = tuple(map(int, input().split()))
moves = 0
arrived = 0
for _ in range(k):
    # 참가자 이동 실행
    for i in range(m):
        if participants[i] == goal:
            continue
        # 행이 다르기 때문에 상하 이동 진행하면 됨
        x, y= participants[i]
        if x != goal[0]:
            nx,ny = x,y
            if goal[0] > x:
                nx += 1
            else:
                nx -= 1
            if field[nx][ny] == 0:
                participants[i] = (nx,ny)
                moves += 1
                continue
        # 높이가 다르기 때문에 좌우 이동하면 됨
        if y != goal[1]:
            nx, ny = x,y
            if goal[1] > y:
                ny+= 1
            else:
                ny-= 1
            if field[nx][ny] == 0:
                participants[i] = (nx,ny)
                moves += 1
                continue
    # 이동 후 참가자 상태 확인(도착지 도착 여부)
    arrived = 0
    for participant in participants:
        if participant == goal:
            arrived += 1
    if arrived == m:
        break
    # 끝나지 않은 경우 회전을 위한 최소 정사각형 구하기
    start, end, length = 0, 0, 0
    end_flag = 0
    for l in range(2,n+1):
        if end_flag:
            break
        for x in range(1,n + 2 - l):
            if end_flag:
                break
            for y in range(1, n + 2 - l):
                nx, ny = x + l -1 , y + l - 1
                if not (x <= goal[0] <= nx and y <= goal[1] <= ny):
                    continue
                flag = 0
                for participant in participants:
                    if x <= participant[0] <= nx and y <= participant[1] <= ny and participant != goal:
                        flag = 1
                        break
                if flag:
                    start, end, length = x,y,l
                    end_flag = 1
                    break
    # 회전 대상 내 벽 내구도 감소
    for i in range(start,start+length):
        for j in range(end,end+length):
            if field[i][j] != 0:
                field[i][j] -= 1
    rfield = [[0]*(n+1) for _ in range(n+1)]
    # 맵 회전
    for x in range(start,start+length):
        for y in range(end,end+length):
            # 부분 회전이므로 회전 수행 전 0으로 변환
            zx,zy = x - start, y - end
            rx,ry = zy, length - zx - 1
            rfield[rx + start][ry+end] = field[x][y]
    for x in range(start,start+length):
        for y in range(end,end+length):
            field[x][y] = rfield[x][y]
    # 참가자 회전
    for i in range(m):
        if start <= participants[i][0] < start+length and end <= participants[i][1] < end+length:
            zx,zy = participants[i][0] - start, participants[i][1]- end
            rx,ry = zy, length - zx - 1
            participants[i] = (rx+start,ry+end)
    # 출구 회전
    zx, zy = goal[0]-start, goal[1] - end
    rx, ry = zy, length - zx - 1
    goal = (rx+start, ry+end)   

print(moves)
print(*goal)
# 부분회전에 유의해야 하는 문제
       