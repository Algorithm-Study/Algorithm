from collections import deque

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
dq = deque()
visited = [[0]*n for _ in range(n)]

def bfs(x, y):
    dq.append((x, y))
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    visited[x][y] = 1
    while dq:
        x, y = dq.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dq.append((nx, ny))
                

ans1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            ans1 += 1
            
            
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
            
visited = [[0]*n for _ in range(n)]
ans2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            ans2 += 1
            
print(ans1, ans2)