from collections import deque
n, l, r = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(n)]
move = 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1
    unite, total = [[x,y]], nations[x][y]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] == 1:
                continue
            if l <= abs(nations[x][y] - nations[nx][ny]) <= r:
                visited[nx][ny] = 1
                queue.append([nx, ny])
                unite.append([nx,ny])
                total += nations[nx][ny]
    return unite, total
while True:
    visited = [[0]*(n) for _ in range(n)]
    moved = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                unite, total = bfs(i,j)
                if len(unite) > 1:
                    after_move = total // len(unite)
                    for x,y in unite:
                        nations[x][y] = after_move
                    moved = True
    if not moved:
        break
    move += 1
print(move) 