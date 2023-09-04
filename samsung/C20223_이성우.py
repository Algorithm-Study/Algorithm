n, m, k = map(int, input().split())
arr = [[0]*(n+1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))


# 팀 별 레일 위치
v = [[] for _ in range(m+1)]

# 팀 별 꼬리 위치 관리
tail = [0]*(m+1)
visited = [[False]*(n+1) for _ in range(n+1)]

# 격자 내 레일에 팀 번호 기재
arr_idx = [[0]*(n+1) for _ in range(n+1)]

answer = 0

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def is_out_range(x, y):
    return not (1 <= x <= n and 1 <= y <= n)

# 초기 레일을 위한 dfs
def dfs(x, y, idx):
    visited[x][y] = True
    arr_idx[x][y] = idx
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_out_range(nx, ny):
            continue
        
        # 경로가 아니거나 들린 경로면 패스
        if arr[nx][ny] == 0 or visited[nx][ny]:
            continue
        
        # 가장 처음 탐색할 때 2가 있는 방향으로 dfs를 진행
        if len(v[idx]) == 1 and arr[nx][ny] != 2:
            continue
        
        v[idx].append((nx, ny))
        if arr[nx][ny] == 3:
            tail[idx] = len(v[idx])
        dfs(nx, ny, idx)


def init():
    cnt = 1
    
    # 레일을 벡터에 저장
    # 머리를 우선 앞에 저장
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] == 1:
                v[cnt].append((i, j))
                cnt += 1

    # dfs를 통해 레일을 벡터에 순서대로 저장
    for i in range(1, m+1):
        x, y = v[i][0]
        dfs(x, y, i)
        
# 각 팀 이동 
def move_all():
    for i in range(1, m+1):
        # 각 팀에 대해 레일을 한 칸씩 뒤로 이동
        tmp = v[i][-1]
        for j in range(len(v[i])-1, 0, -1):
            v[i][j] = v[i][j-1]
        v[i][0] = tmp
        
    for i in range(1, m+1):
        for j, (x, y) in enumerate(v[i]):
            if j == 0:
                arr[x][y] = 1
            elif j < tail[i] - 1:
                arr[x][y] = 2
            elif j == tail[i] - 1:
                arr[x][y] = 3
            else:
                arr[x][y] = 4
                
# (x, y) 지점에 공이 닿았을 때의 점수를 계산
def get_point(x, y):
    global answer
    idx = arr_idx[x][y]
    cnt = v[idx].index((x, y))
    answer += (cnt+1)**2
    
# turn 번째 라운드의 공을 던진다
# 공을 던졌을 때 이를 받은 팀의 번호를 반환
def throw_ball(turn):
    t = (turn-1) % (4*n) + 1
    
    if t <= n:
        # 1~n 라운드 왼쪽에서 오른쪽
        for i in range(1, n+1):
            if 1 <= arr[t][i] and arr[t][i] <= 3:
                # 사람이 있는 첫 번째 지점 탐색
                # 찾게 되면 점수를 확인 후 찾은 팀의 번호 저장
                get_point(t, i)
                return arr_idx[t][i]
    
    elif t <= 2*n:
        # n+1 ~ 2n 라운드 아래에서 위로
        t -= n
        for i in range(1, n+1):
            if 1 <= arr[n+1-i][t] and arr[n+1-i][t] <= 3:
                get_point(n+1-i, t)
                return arr_idx[n+1-i][t]
    
    elif t <= 3*n:
        # 2n+1 ~ 3n 라운드 오른쪽에서 왼쪽으로
        t -= 2*n
        for i in range(1, n+1):
            if 1 <= arr[n+1-t][n+1-i] and arr[n+1-t][n+1-i] <= 3:
                get_point(n+1-t, n+1-i)
                return arr_idx[n+1-t][n+1-i]

    else:
        # 3n+1 ~ 4n 라운드 위에서 아래
        t -= 3*n
        for i in range(1, n+1):
            if 1 <= arr[i][n+1-t] and arr[i][n+1-t] <= 3:
                get_point(i, n+1-t)
                return arr_idx[i][n+1-t]
            
    # 공이 지나가면 0 반환
    return 0

# 공을 획득한 팀은 순서 변경
def reverse(got_ball_idx):
    if got_ball_idx == 0:
        return
    
    idx = got_ball_idx
    
    new_v = []
    
    for j in range(tail[idx]-1, -1, -1):
        new_v.append(v[idx][j])

    for j in range(len(v[idx])-1, tail[idx]-1, -1):
        new_v.append(v[idx][j])
        
    v[idx] = new_v[:]
    
    # 벡터에 저장한 정보를 바탕으로 보드의 표기 변경
    for j, (x, y) in enumerate(v[idx]):
        if j == 0:
            arr[x][y] = 1
        elif j < tail[idx] - 1:
            arr[x][y] = 2
        elif j == tail[idx] - 1:
            arr[x][y] = 3
        else:
            arr[x][y] = 4
            
init()
for i in range(1, k+1):
    # 머리를 따라 이동
    move_all()
    
    # i 번째 라운드 및 점수 획득
    got_ball_idx = throw_ball(i)
    
    # 공을 획득한 팀 방향 변경
    reverse(got_ball_idx)

print(answer)