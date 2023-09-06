from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[float('inf') for _ in range(n)] for _ in range(n)]

q = deque()
q.append((0, 0))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited[0][0] = 0

while q:
    x, y = q.popleft()
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == float('inf'):
            if arr[nx][ny] == 1:
                q.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y]
            else:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[n-1][n-1])