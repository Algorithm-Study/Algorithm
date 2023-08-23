from collections import deque
import copy

arr = [[] for _ in range(4)]

for i in range(4):
    fish = deque(map(int, input().split()))
    for _ in range(4):
        a, b = fish.popleft(), fish.popleft()
        arr[i].append([a, b-1])
        
max_score = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(sx, sy, score, arr):
    global max_score
    score += arr[sx][sy][0]
    max_score = max(max_score, score)
    arr[sx][sy][0] = 0
    
    for f in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if arr[x][y][0] == f:
                    fx, fy = x, y
                    break
                
        if fx == -1 and fy == -1:
            continue
        fd = arr[fx][fy][1]
        
        for i in range(8):
            nd = (fd+i)%8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            if not(0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            
            arr[fx][fy][1] = nd
            arr[fx][fy], arr[nx][ny] = arr[nx][ny], arr[fx][fy]
            break
            
    sd = arr[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[sd]*i
        ny = sy + dy[sd]*i
        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(arr))
            
dfs(0, 0, 0, arr)
print(max_score)