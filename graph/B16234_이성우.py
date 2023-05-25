from collections import deque
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a: int, b: int) -> list:
    que = deque()
    que.append((a,b))
    tmp = [(a,b)]
    
    while que:
        x, y = que.popleft()
        
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    que.append((nx,ny))
                    tmp.append((nx,ny))
                    visited[nx][ny] = 1

    return tmp

while True:
    visited = [[0]*(N) for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union = bfs(i,j)
                
                if len(union) > 1:
                    flag = 1
                    num = sum(arr[x][y] for x, y in union) // len(union)
                
                    for x, y in union:
                        arr[x][y] = num
    
    if flag == 0:
        break
    
    answer += 1
    
print(answer)