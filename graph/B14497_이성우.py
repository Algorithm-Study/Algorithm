import sys
from collections import deque
input= sys.stdin.readline

# 변수 초기화
n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
distance = [[-1]*m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()

# bfs 구현
def bfs(x, y):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                if arr[nx][ny] == '1' or arr[nx][ny] == '#':
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
                elif arr[nx][ny] == '0':
                    distance[nx][ny] = distance[x][y]
                    q.appendleft((nx, ny))
    return distance[x2-1][y2-1]


# 조건 탐색
q.append((x1-1, y1-1))
distance[x1-1][y1-1] = 0
print(bfs(x1-1, y1-1))