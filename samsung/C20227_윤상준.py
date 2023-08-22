from collections import deque
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
stores = list(list(map(int,input().split())) for _ in range(M))
for idx in range(len(stores)):
    r,c = stores[idx]
    stores[idx] = [r-1,c-1]

base_store = [[0]*N for _ in range(N)] # base camp와 store 도착했을 경우 저장
people_pos = [[[] for _ in range(N)] for _ in range(N)]

bases = deque()
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            bases.append((r,c))

# 상,좌,우,하(우선순의)
dr = [-1,0,0,1]
dc = [0,-1,1,0]

def in_range(in_r,in_c):
    if 0 <= in_r < N and 0 <= in_c < N:
        return True
    return False

def is_empty(is_r,is_c):
    if base_store[is_r][is_c] != -1:
        return True
    return False

def bfs(now_r,now_c,n_m):
    dst_r,dst_c = stores[n_m-1]
    q = deque()
    cnt = 0
    q.append((now_r,now_c,cnt,-1))
    visited = [[0]*N for _ in range(N)]
    visited[now_r][now_c] = 1
    # print(f"현재({now_r},{now_c}), {n_m} 목적지 : ({dst_r},{dst_c})")
    while q:
        r,c,cnt,direction = q.popleft()
        if r == dst_r and c == dst_c:
            return direction,cnt
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if in_range(nr,nc) and is_empty(nr,nc) and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if cnt == 0: # 첫번째 step이면 step에 해당하는 방향을 direction으로 저장
                    q.append((nr,nc,cnt+1,i))
                else: # 두번째 이상 step에서는 첫번째 step을 계속 가져갈 수 있도록 함
                    q.append((nr,nc,cnt+1,direction))
    return -1,-1 # 현재 위치에서 목적지로 갈 수 없는 경우

def move_to_store():
    global arrive_cnt
    people = []
    for r in range(N):
        for c in range(N):
            if people_pos[r][c]:
                if len(people_pos[r][c]) > 1: # 한 위치에 2명 이상 있는 경우
                    for PERSON_NUMBER in people_pos[r][c]:
                        people.append((PERSON_NUMBER,r,c))
                else: # 한 위치에 한명만 있는 경우
                    people.append((people_pos[r][c][0],r,c)) # number,r,c 저장

    for p_n,r,c in people:
        direction,_ = bfs(r,c,p_n)
        nr = r + dr[direction]
        nc = c + dc[direction]
        dst_r,dst_c = stores[p_n-1]
        if nr == dst_r and nc == dst_c:
            base_store[nr][nc] = -1
            arrive_cnt += 1
            people_pos[r][c].remove(p_n)
        else:
            people_pos[r][c].remove(p_n)
            people_pos[nr][nc].append(p_n)

def move_to_base(person_n):
    if not person_n:
        return
    search = []
    for r,c in bases:
        if base_store[r][c] != -1:
            _,cnt = bfs(r,c,person_n)
            if cnt == -1:
                continue
            search.append([cnt,r,c])
    search.sort(key=lambda x : (x[0],x[1],x[2]))
    _,r,c = search[0]
    base_store[r][c] = -1
    people_pos[r][c].append(person_n)

def actions():
    move_to_store()
    move_to_base(input_n)

time = 0
arrive_cnt = 0

while True:
    if arrive_cnt == M:
        print(time)
        break
    if time < M:
        input_n = time + 1
    else:
        input_n = 0
    actions()
    time += 1