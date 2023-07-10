import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())

arr = [list(input().strip()) for _ in range(r)]

f_q, j_q = deque(), deque()
f_visited, j_visited = [[0]*c for _ in range(r)], [[0]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'J':
            j_q.append((i, j))
            j_visited[i][j] = 1
        elif arr[i][j] == 'F':
            f_q.append((i, j))
            f_visited[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  

def bfs():
    while f_q:
        x, y = f_q.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < r and 0 <= ny < c:
                if not f_visited[nx][ny] and arr[nx][ny] != '#':
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_q.append((nx, ny))
 
    while j_q:
        x, y = j_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] != '#' and not j_visited[nx][ny]:
                    if not f_visited[nx][ny] or f_visited[nx][ny] > j_visited[x][y] + 1:
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_q.append((nx, ny))
            else:
                return j_visited[x][y]
 
    return 'IMPOSSIBLE'

print(bfs())
