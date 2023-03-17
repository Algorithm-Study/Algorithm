# 2차워과 동일한 방식으로 작동 -> 3차원에 맞도록 수정만 하면 성공!!!
# bfs 방식
from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
data = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = [0, 0, -1, 0, 1, 0]
dy = [0, 0, 0, 1, 0, -1]
dz = [1, -1, 0, 0, 0, 0]
result = 0
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                queue.append((i, j, k))

def tomato():
    global result
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx< 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                continue
            if data[nz][nx][ny] == -1:
                continue
            if data[nz][nx][ny] == 0:
                data[nz][nx][ny] = data[z][x][y] + 1
                queue.append((nz, nx, ny))
    result = max(max(map(max, box)) for box in data) - 1         


tomato()
#print(data)
zero_count = 0
for box in data:
    for b in box:
        if 0 in b:
            result = -1
print(result)