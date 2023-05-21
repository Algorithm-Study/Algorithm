from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()
visited = [[False]*m for _ in range(n)]
answer = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i, j))
            visited[i][j] = True
            answer[i][j] = 0

        if arr[i][j] == 0:
            answer[i][j] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
            q.append((nx, ny))
            visited[nx][ny] = True
            answer[nx][ny] = answer[x][y] + 1

for _ in answer:
    print(*_)