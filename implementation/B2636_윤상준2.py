from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n,m = map(int, input().split())
cheese = 0
field = []
time, before = 0, 0
for i in range(n):
    line = list(map(int, input().split()))
    cheese += sum(line)
    field.append(line)
while cheese:
    time += 1
    before = cheese
    queue = deque()
    queue.append((0, 0))
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    melt = []
    # 녹는 대상 찾기
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny] == 1:
                continue
            visited[nx][ny] = 1
            if field[nx][ny] == 1:
                melt.append((nx, ny))
            else:
                queue.append((nx, ny))
    cheese -= len(melt)
    # 녹는 대상 제거
    for x, y in melt:
        field[x][y] = 0
print(time)
print(before)
