from collections import deque

arr = [list(input()) for _ in range(12)]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

answer = 0
cnt = True
while cnt:
    q = deque()
    cnt = False
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if visited[i][j] == False and arr[i][j] != '.':
                tmp = []
                q.append((i, j))
                visited[i][j] = True
                tmp.append((i, j))
                target = arr[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 12 and 0 <= ny < 6 and arr[nx][ny] == target and visited[nx][ny] == False:
                            q.append((nx, ny))
                            tmp.append((nx, ny))
                            visited[nx][ny] = True
                if len(tmp) >= 4:
                    for x, y in tmp:
                        arr[x][y] = '.'
                    cnt = True
    
    if cnt == True:
        answer += 1
        
    for j in range(6):
        idx = 11
        for i in range(11, -1, -1):
            if arr[i][j] != '.':
                arr[idx][j], arr[i][j] = arr[i][j], arr[idx][j]
                idx -= 1
            
print(answer)
