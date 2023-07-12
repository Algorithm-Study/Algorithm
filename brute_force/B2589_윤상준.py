from collections import deque
n, m = map(int, input().split())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
field = []
result = 0
for _ in range(n):
    field.append(list(input()))
for i in range(n):
    for j in range(m):
        if field[i][j] == 'L':
            visited = [[0]*m for _ in range(n)]
            queue = deque()
            queue.append((i,j))
            visited[i][j] = 1
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >=n or ny >=m or visited[nx][ny] != 0 or field[nx][ny] == 'W':
                        continue
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
            result = max(result,max([max(visited[x]) for x in range(n)]))
print(result-1)

#L인 경우 BFS 탐색을 진행해서 가장 거리가 먼 경우 출력하면 되는 문제