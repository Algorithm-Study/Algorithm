from collections import deque
n, m = map(int,input().split())
field = []
visited = [[-1]*m for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    if 2 in line:
        start = [i, line.index(2)]
    field.append(line)
dx = [-1, 0 ,1 , 0]
dy = [0, -1, 0, 1]
queue = deque()
queue.append(start)
visited[start[0]][start[1]] = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >=n or ny >=m or visited[nx][ny] != -1 or field[nx][ny] == 0:
            continue
        visited[nx][ny] = visited[x][y] + 1
        queue.append([nx,ny])
for i in range(n):
    for j in range(m):
        if field[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
# 갈 수 없는 곳에 대한 처리만 하면 쉽게 해결 가능