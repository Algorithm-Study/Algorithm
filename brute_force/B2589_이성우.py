from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
answers = []

def bfs(i,j):
    answer = 0
    dq = deque()
    dq.append([i, j])

    visited = [[0]*m for _ in range(n)]
    
    visited[i][j] = 1
    
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] != 'W':
                visited[nx][ny] = visited[x][y] + 1
                answer = visited[nx][ny]
                dq.append([nx, ny])
                
    return answer

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            answers.append(bfs(i,j))
            
print(max(answers)-1)