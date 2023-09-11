n, m, h, k = map(int, input().split())

# 각 칸에 있는 도망자 정보
hiders = [[[] for _ in range(n)] for _ in range(n)]
next_hiders = [[[] for _ in range(n)] for _ in range(n)]
tree = [[False]*n for _ in range(n)]

# 정방향 기준, 현재 위치에서 술래가 움직여야 할 방향
seeker_next_dir = [[0]*n for _ in range(n)]

# 역방향 기준, 현재 위치에서 술래가 움직여야 할 방향
seeker_rev_dir = [[0]*n for _ in range(n)]

# 술래 위치 및 정방향, 역방향
seeker_pos = (n//2, n//2)
forward = True

ans = 0

# 술래 정보
for _ in  range(m):
    x, y, d = map(int, input().split())
    hiders[x-1][y-1].append(d)

# 나무 정보
for _ in range(h):
    x, y = map(int, input().split())
    tree[x-1][y-1] = True
    

# 정중앙부터 끝까지 움직이는 경로
def initialize_seeker_path():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 시작 위치 및 방향
    # 해당 방향으로 이동할 횟수 설정
    curr_x, curr_y = n//2, n//2
    move_dir, move_num = 0, 1
    
    while curr_x or curr_y:

        for _ in range(move_num):
            seeker_next_dir[curr_x][curr_y] = move_dir
            curr_x, curr_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]
            seeker_rev_dir[curr_x][curr_y] = move_dir + 2 if move_dir < 2 else move_dir - 2
            
            # (0, 0)으로 오면 멈춤
            if not curr_x and not curr_y:
                break
            
        # 방향 전환
        move_dir = (move_dir + 1)%4
        
        # 만약 현재 방향이 위 혹은 아래가 된 경우
        # 특정 방향으로 움직이는 횟수 1 증가
        if move_dir == 0 or move_dir == 2:
            move_num += 1
                
# 격자 내에 있는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def hider_move(x, y, move_dir):
    dxs, dys = [0, 0, 1, -1], [-1, 1, 0, 0]

    nx, ny = x + dxs[move_dir], y + dys[move_dir]

    # 격자를 벗어나면 방향 전환
    if not in_range(nx, ny):
        move_dir = 1 - move_dir if move_dir < 2 else 5 - move_dir
        nx, ny = x + dxs[move_dir], y + dys[move_dir]

    # 그 다음 위치에 술래가 없으면 이동
    if (nx, ny) != seeker_pos:
        next_hiders[nx][ny].append(move_dir)
    else:
        next_hiders[x][y].append(move_dir)

    
def dist_from_seeker(x, y):
    seeker_x, seeker_y = seeker_pos
    return abs(seeker_x - x) + abs(seeker_y - y)


def hider_move_all():
    # next_hider 초기화
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []
            
    # hider 이동        
    for i in range(n):
        for j in range(n):
            # 술래와 거리 3 이내인 도망자 이동
            if dist_from_seeker(i, j ) <= 3:
                for move_dir in hiders[i][j]:
                    hider_move(i, j, move_dir)
            # 3 보다 크면 대기
            else:
                for move_dir in hiders[i][j]:
                    next_hiders[i][j].append(move_dir)

    # next_hider값 이동
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]


# 현재 술래가 바라보는 방향 가져온다
def get_seeker_dir():
    x, y = seeker_pos
    
    move_dir = 0
    if forward:
        move_dir = seeker_next_dir[x][y]
    else:
        move_dir = seeker_rev_dir[x][y]
    return move_dir


def check_facing():
    global forward
    
    # 정방향으로 끝에 닿은 경우 방향 변경
    if seeker_pos == (0, 0) and forward:
        forward = False
    # 역방향으로 끝에 닿은 경우 방향 변경
    if seeker_pos == (n//2, n//2) and not forward:
        forward = True
        
def seeker_move():
    global seeker_pos
    
    x, y = seeker_pos
    
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    move_dir = get_seeker_dir()
    
    # 술래 이동
    seeker_pos = x + dxs[move_dir], y + dys[move_dir]

    # 끝에 도달했다면 방향 변경
    check_facing()
    

def get_score(t):
    global ans
    
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 현재 술래 위치
    x, y = seeker_pos
    
    # 술래 방향
    move_dir = get_seeker_dir()
    
    # 3칸 확인
    for dist in range(3):
        nx, ny = x + dist * dxs[move_dir], y + dist * dys[move_dir]

        # 격자를 벗어나지 않고 나무가 없으면 도망자 제거
        if in_range(nx, ny) and not tree[nx][ny]:
            # 해당 위치의 도망자 수만큼 점수 획득
            ans += t * len(hiders[nx][ny])

            # 도망자 제거
            hiders[nx][ny] = []
            
# 초기값 설정
initialize_seeker_path()

for t in range(1, k+1):
    hider_move_all()
    seeker_move()
    get_score(t)
    
print(ans)