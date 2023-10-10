dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
from collections import deque
n, m = map(int, input().split())
field = []
water = deque()
biber = deque()
goal = [0,0]
b_visited = [[0]*m for _ in range(n)]
w_visited = [[0]*m for _ in range(n)]
# 입력 받기
for i in range(n):
    line = list(input())
    for j in range(m):
        # 목적지
        if line[j] == 'D':
            goal = [i,j]
        elif line[j] == '*':
            water.append((i,j))
            w_visited[i][j] = 1
        elif line[j] == 'S':
            biber.append((i, j, 0))
            b_visited[i][j] = 1
    field.append(line)
while biber:
    # 물 먼저 불어나기
    new_water = []
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >=m or w_visited[nx][ny]:
                continue
            if field[nx][ny] != 'X' and field[nx][ny] != 'D':
                field[nx][ny] = '*'
                w_visited[nx][ny] = 1
                new_water.append((nx,ny))
    
    water = deque(new_water)
    # 비버 이동하기
    new_biber = []
    while biber:
        x, y, cnt = biber.popleft()
        if field[x][y] == 'D':
            print(cnt)
            exit()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >=m or b_visited[nx][ny]:
                continue
            if field[nx][ny] != 'X' and field[nx][ny] != '*':
                b_visited[nx][ny] = 1
                new_biber.append((nx,ny, cnt + 1))
    biber = deque(new_biber)
print('KAKTUS')