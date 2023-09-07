n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]


def dfs(x, y, sx, sy):
    visited[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == arr[x][y]:
            if visited[nx][ny] == False:
                if dfs(nx, ny, x, y):
                    return True
            elif (nx, ny) != (sx, sy):
                    return True
            
    return False

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            if dfs(i, j, -1, -1):
                print('Yes')
                exit()
print('No')