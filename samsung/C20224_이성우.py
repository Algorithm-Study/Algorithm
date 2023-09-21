n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
death = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]
for _ in range(m):
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:
                cnt = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                        cnt += 1
                arr[x][y] += cnt
        
    growth = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:
                cnt = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 and death[nx][ny] == 0:
                        cnt += 1
                        
                for d in range(4):
                    nx, ny = x +dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 and death[nx][ny] == 0:
                        growth[nx][ny] += arr[x][y]//cnt
                        
    for x in range(n):
        for y in range(n):
            arr[x][y] += growth[x][y]

    max_cnt = -1
    mx, my = -1, -1
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:
                cnt = arr[x][y]
                for d in range(4, 8):
                    for r in range(1, k+1):
                        nx, ny = x + dx[d]*r, y + dy[d]*r
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] <= 0:
                                break
                            
                            cnt += arr[nx][ny]
                    
                if cnt > max_cnt:
                    max_cnt = cnt
                    mx, my = x, y

    for d in range(4, 8):
        for r in range(1, k+1):
            nx, ny = mx + dx[d]*r, my + dy[d]*r
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] <= 0:
                    death[nx][ny] = c+1
                    break

                answer += arr[nx][ny]
                arr[nx][ny] = 0
                death[nx][ny] = c+1
                
    if (mx, my) != (-1, -1):
        answer += arr[mx][my]
        arr[mx][my] = 0
        death[mx][my] = c+1
    
    for x in range(n):
        for y in range(n):
            if 0 < death[x][y]:
                death[x][y] -= 1
            
print(answer)
