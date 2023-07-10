from collections import deque
n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
field = []
queue = deque()
fire = deque()
visited = [[0]*m for _ in range(n)]
visited2 = [[0]*m for _ in range(n)]
# 불과 지훈이의 위치 정보 추가
for i in range(n):
    line = list(input())
    field.append(line)
    for j in range(m):
        if line[j] == 'J':
            queue.append((i, j))
            visited[i][j] = 1
        elif line[j] == 'F':
            fire.append((i, j))
            visited2[i][j] = 1
# 불의 BFS
while fire:
    x, y = fire.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited2[nx][ny]:
            continue
        if field[nx][ny] != '#':
            visited2[nx][ny] = visited2[x][y] + 1
            fire.append((nx, ny))
# 지훈이의 BFS
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            print(visited[x][y])
            exit()
        elif visited[nx][ny]:
            continue
        if field[nx][ny] != '#':
            if not visited2[nx][ny] or visited2[nx][ny] > visited[x][y] + 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
else:
    print('IMPOSSIBLE')

# 두 상황을 개별로 bfs 진행하는 것이 더 쉬움