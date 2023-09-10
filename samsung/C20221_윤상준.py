# 위 오른쪽 아래 왼쪽
dx = [-1,0,1,0]
dy = [0,1,0,-1]
# n: 필드 크기, m: 도망자 수, h: 나무의 수, k: 전체 턴 수
n,m,h,K = map(int, input().split())
move = []
# 술래 움직이는 횟수
for i in range(1,n+1):
    move.append(i)
    move.append(i)
# catcher : 술래 위치, runner: 도망자 정보(x,y,방향, 잡혔는지 여부)
catcher, runner = (n//2, n//2),[]
catcher_move, catcher_move_count, catcher_dir, catcher_snail = 0,0,0,1
for _ in range(m):
    x,y,dir = map(int, input().split())
    x-=1
    y-=1 
    runner.append((x,y,dir,0))
field = [[0]*n for _ in range(n)]
for _ in range(h):
    x,y = map(int, input().split())
    field[x-1][y-1] = 1
score = 0
for turn in range(1,K+1):
    # 도망자 이동
    for idx in range(len(runner)):
        x,y,dir,status = runner[idx]
        #잡힌 경우(이동X)
        if status == 1:
            continue
        # 술래와의 거리가 3보다 큰 경우(이동 X)
        if abs(catcher[0] - x) + abs(catcher[1]-y) > 3:
            continue
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 격자를 벗어나는 경우(방향 전환)
        if nx < 0 or ny < 0 or nx >= n or ny >=n:
            dir = dir ^ 2
            nx = x + dx[dir]
            ny = y + dy[dir]
        # 위치에 술래가 존재하지 않는 경우 이동
        if (nx,ny) != (catcher):
            runner[idx] = (nx,ny,dir,status)
    # 술래 이동
    cx = catcher[0] + dx[catcher_dir]
    cy = catcher[1] + dy[catcher_dir]
    catcher_move_count += 1
    # 끝까지 도달한 경우
    if (cx,cy) == (0,0):
        catcher_snail *= -1
        catcher_move_count = move[catcher_move] - catcher_move_count
        catcher_dir = catcher_dir^2
    # 다시 처음으로 되돌아온 경우
    if (cx,cy) == (n//2, n//2):
        catcher_snail *= -1
        catcher_move_count = 0
        catcher_dir = catcher_dir^2
    catcher = (cx,cy)
    # 달팽이 이동과정에서 회전해야 할 경우
    if catcher_move_count == move[catcher_move]:
        catcher_move_count = 0
        catcher_dir = (catcher_dir + catcher_snail)%4
        catcher_move += catcher_snail
    # 도망자 잡을 수 있는지 체크
    looking = []
    # 위
    if catcher_dir == 0:
        for scope in range(catcher[0],max(-1,catcher[0]-3),-1):
            looking.append((scope, catcher[1]))
    # 오른쪽
    elif catcher_dir == 1:
        for scope in range(catcher[1],min(n, catcher[1]+3)):
            looking.append((catcher[0], scope))
    # 아래
    elif catcher_dir == 2:
        for scope in range(catcher[0],min(n, catcher[0]+3)):
            looking.append((scope, catcher[1]))
    # 왼쪽
    else:
        for scope in range(catcher[1],max(-1,catcher[1]-3),-1):
            looking.append((catcher[0], scope))
    # 점수 획득
    for idx, run in enumerate(runner):
        # 시야 내에 존재하고 나무에 가려지지 않았으며 잡히지 않은 경우 점수 획득
        if (run[0],run[1]) in looking and field[run[0]][run[1]] == 0 and run[3] == 0:
            score += turn
            runner[idx] = (runner[idx][0], runner[idx][1], runner[idx][2], 1)
print(score)

