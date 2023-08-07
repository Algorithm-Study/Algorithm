from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rec = [[0 for _ in range(m)] for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
dxs2 = [0, 0, 0, -1, -1, -1, 1, 1, 1]
dys2 = [0, -1, 1, 0, -1, 1, 0, -1, 1]

turn = 0

visited = [[0 for _ in range(m)] for _ in range(n)]
back_x = [[0 for _ in range(m)] for _ in range(n)]
back_y = [[0 for _ in range(m)] for _ in range(n)]

is_active = [[False for _ in range(m)] for _ in range(n)]

class Turret:
    def __init__(self, x, y, r, p):
        self.x = x
        self.y = y
        self.r = r
        self.p = p
        
live_terret = []

def init():
    global turn
    
    turn += 1
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            is_active[i][j] = False
            

def awake():
    live_terret.sort(key = lambda x : (x.p, -x.r, -(x.x + x.y), -x.y))

    weak_turret = live_terret[0]
    x = weak_turret.x
    y = weak_turret.y

    arr[x][y] += n+m
    rec[x][y] = turn
    weak_turret.p = arr[x][y]
    weak_turret.r = rec[x][y]
    is_active[x][y] = True

    live_terret[0] = weak_turret
    
def laser_attack():
    weak_turret = live_terret[0]
    start_x = weak_turret.x
    start_y = weak_turret.y
    power = weak_turret.p
    
    strong_turret = live_terret[-1]
    end_x = strong_turret.x
    end_y = strong_turret.y
    
    q = deque()
    visited[start_x][start_y] = True
    q.append((start_x, start_y))

    can_attack = False
    
    while q:
        x, y = q.popleft()
        
        if x == end_x and y == end_y:
            can_attack = True
            break
        
        for dx, dy in zip(dxs, dys):
            nx = (x+dx+n) % n
            ny = (y+dy+m) % m
            
            if visited[nx][ny] or arr[nx][ny] == 0:
                continue
            
            visited[nx][ny] = True
            back_x[nx][ny] = x
            back_y[nx][ny] = y
            q.append((nx, ny))

    if can_attack:
        arr[end_x][end_y] = max(arr[end_x][end_y] - power, 0)
        is_active[end_x][end_y] = True
        
        cx = back_x[end_x][end_y]
        cy = back_y[end_x][end_y]

        while not (cx == start_x and cy == start_y):
            arr[cx][cy] = max(arr[cx][cy] - power//2, 0)
            is_active[cx][cy] = True
            
            next_cx = back_x[cx][cy]
            next_cy = back_y[cx][cy]
            
            cx = next_cx
            cy = next_cy
            
    return can_attack

def bomb_attack():
    weak_turret = live_terret[0]
    start_x = weak_turret.x
    start_y = weak_turret.y
    power = weak_turret.p
    
    strong_turret = live_terret[-1]
    end_x = strong_turret.x
    end_y = strong_turret.y
    
    for dx2, dy2 in zip(dxs2, dys2):
        nx = (end_x+dx2+n) % n
        ny = (end_y+dy2+m) % m
        
        if nx == start_x and ny == start_y:
            continue
        
        if nx == end_x and ny == end_y:
            arr[nx][ny] = max(arr[nx][ny] - power, 0)
        else:
            arr[nx][ny] = max(arr[nx][ny] - power//2, 0)
        is_active[nx][ny] = True
        
def reserve():
    for i in range(n):
        for j in range(m):
            if is_active[i][j] or arr[i][j] == 0:
                continue
            arr[i][j] += 1
            
for _ in range(k):
    live_terret = []
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                new_turret = Turret(i, j, rec[i][j], arr[i][j])
                live_terret.append(new_turret)

    if len(live_terret) <= 1:
        break
    
    init()
    awake()
    is_suc = laser_attack()
    if not is_suc:
        bomb_attack()
    reserve()
    
answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, arr[i][j])

print(answer)

