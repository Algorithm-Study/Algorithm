## pypy 통과 코드
from collections import deque
n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
year = 0
while True:
    after = [[0]*m for _ in range(n)]
    # 빙산 1년 후 계산 -> 완탐
    for i in range(n):
        for j in range(m):
            if sea[i][j] != 0:
                water = 0
                for k in range(4):
                    nx = i+ dx[k]
                    ny = j+ dy[k]
                    if nx <0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if sea[nx][ny] == 0:
                        water += 1
                after[i][j] = max(sea[i][j] - water, 0)
    # 빙산 갱신
    sea = after[:]
    # 빙산 갯수 계산 -> bfs
    visited = [[0]*m for _ in range(n)]
    block = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and sea[i][j] != 0:
                visited[i][j] = 1
                queue = deque()
                queue.append([i,j])
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx <0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == 1 or sea[nx][ny] == 0:
                            continue
                        visited[nx][ny] = 1
                        queue.append([nx,ny])
                block += 1
    year += 1
    if block == 0:
        print(0)
        break
    if block >= 2:
        print(year)
        break
### pypy, python 통과코드(아래)
import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def bfs(x,y):
    visited[x][y] = 1
    queue = deque()
    queue.append((x,y))
    melt = []
    while queue:
        x,y = queue.popleft()
        water = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx <0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == 1:
                continue
            if sea[nx][ny] == 0:
                water += 1
            else:
                queue.append((nx,ny))
                visited[nx][ny] = 1
        if water > 0:
            melt.append((x,y,water))
    for x,y,water in melt:
        sea[x][y] = max(sea[x][y]- water, 0)
    return 1

n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]
year = 0

while True:
    visited = [[0] * m for _ in range(n)]
    removal = []
    block = 0
    for i in range(n):
        for j in range(m):
            if sea[i][j] != 0 and visited[i][j] == 0:
                block += bfs(i,j)
    if block == 0:
        print(0)
        break       
    if block >= 2:
        print(year)
        break
    year += 1
# 모두 녹아 없어지는 경우 끝나도록 해야 TLE 안에 문제 해결 가능