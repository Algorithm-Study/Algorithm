from collections import deque

arr = [[0 for _ in range(501)] for _ in range(501)]
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2)+1):
        for j in range(min(y1, y2), max(y1, y2)+1):
            arr[i][j] = -1
m = int(input())
for _ in range(m):
    x3, y3, x4, y4 = map(int, input().split())
    for i in range(min(x3, x4), max(x3, x4)+1):
        for j in range(min(y3, y4), max(y3, y4)+1):
            arr[i][j] = 1
            
arr[0][0] = 0
q = deque()
q.append((0, 0))
visited = [[[0, 0] for _ in range(501)] for _ in range(501)]
visited[0][0] = [1, 0]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

while q:
    x, y = q.popleft()
    
    if x == 500 and y == 500:
        print(-visited[x][y][1])
        break
    
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        
        if 0 <= nx < 501 and 0 <= ny < 501 and arr[nx][ny] != 1 and visited[nx][ny][0] == 0:
            if arr[nx][ny] == 0:
                q.appendleft((nx, ny))
            else: # arr[nx][ny] == 1:
                q.append((nx, ny))
            visited[nx][ny] = [1, visited[x][y][1]+ arr[nx][ny]]
else:
    print(-1)