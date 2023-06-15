from collections import deque

n, m = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]
answer = 0
    
def melt(arr, ice):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    tmp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            cnt = 0
            for d in range(4):
                if 0 <= i+dx[d] < n and 0 <= j+dy[d] < m \
                    and arr[i+dx[d]][j+dy[d]] == 0:
                    cnt += 1
            tmp[i][j] = max(arr[i][j] - cnt, 0)
            if tmp[i][j]:
                ice.append((i,j))
    arr = tmp[:]
    return arr, ice
    
def bfs(u, v, part):
    q = deque()
    q.append((u,v))
    visited[u][v] = True
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0 \
                and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
    part += 1
    return part

while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer += 1
    part = 0
    ice = []
    arr, ice = melt(arr, ice)

    for i in ice:
        ix, iy = i
        if visited[ix][iy] == False:
            part = bfs(ix, iy, part)

        if part >= 2:
            print(answer)
            exit()
            
    if part == 0:
        print(0)
        exit()