from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

q = deque()
q.append((0, 0, 0))
visited[0][0] = True

while q:
    x, y, c = q.popleft()
    
    if x == n-1 and y == m-1:
        answer = c
        break

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
            visited[nx][ny] = True
            if arr[nx][ny] == 0:
                q.appendleft((nx, ny, c))
            else:
                q.append((nx, ny, c+1))
                
print(answer)