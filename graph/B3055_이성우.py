from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
water = deque()
dochi = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]
answer = 'KAKTUS'

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            dochi.append([i, j])
        if arr[i][j] == '*':
            water.append([i, j])
            
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(dochi, water):
    global answer
    while dochi:
        n_water = deque()
        while water:
            wx, wy = water.popleft()
            for d in range(4):
                nwx, nwy = wx + dx[d], wy + dy[d]
                if 0 <= nwx < n and 0 <= nwy < m:
                    if arr[nwx][nwy] == '.' or arr[nwx][nwy] == 'S':
                        arr[nwx][nwy] = '*'
                        n_water.append([nwx, nwy])
        water = n_water

        n_dochi = deque()
        while dochi:    
            x, y = dochi.popleft()
            
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    if arr[nx][ny] == 'D':
                        answer = visited[x][y] + 1
                    if  arr[nx][ny] == '.' or arr[nx][ny] == 'D':
                        arr[nx][ny] = 'S'
                        n_dochi.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1
        dochi = n_dochi

bfs(dochi, water)
print(answer)