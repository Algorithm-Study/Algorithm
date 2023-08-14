from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
answer = 0

while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dq = deque()
    dq.append((0, 0))
    visited[0][0] = 1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if arr[nx][ny] >= 1:
                    arr[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0
                cnt = 1
            elif arr[i][j] == 2:
                arr[i][j] = 1
    if cnt == 1:
        answer += 1
    else:
        break
    
print(answer)
