from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
time = cnt = 0

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
visited = [[0 for _ in range(m)] for _ in range(n)]
dq = deque((0, 0))
visited[0][0] = 1

while True:
    tmp = []
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    dq.append((nx, ny))
                else:
                    tmp.append((nx, ny))
                visited[nx][ny] = 1
    if tmp:
        for i, j in tmp:
            arr[i][j] = 0
            dq.append((i, j))
        cnt = len(tmp)
        time += 1
    else:
        print(time)
        print(cnt)
        break
