from collections import deque
import sys
sys.setrecursionlimit(10**6)
m, n = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            queue.append((i,j))

def tomato():
    global result
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx< 0 or ny < 0 or nx >= n or ny >=m:
                continue
            if data[nx][ny] == -1:
                continue
            if data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx, ny))
                result = max(data[nx][ny], result)


tomato()
if sum(x.count(0) for x in data) > 0:
    print(-1)
else:
    if result == 0:
        print(result)
    else:
        print(result - 1)