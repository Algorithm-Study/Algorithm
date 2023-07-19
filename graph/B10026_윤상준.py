from collections import deque
n = int(input())
field = [list(input()) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited_able = [[0 for _ in range(n)] for _ in range(n)]
visited_disable = [[0 for _ in range(n)] for _ in range(n)]
## 정상인
def bfs(color, x, y, flag):
    queue = deque()
    queue.append((color, x, y))
    if flag == 0:
        visited_able[x][y] = 1
    else:
        visited_disable[x][y] = 1
    while queue:
        prev, x, y = queue.popleft()
        for way in range(4):
            nx = x + dx[way]
            ny = y + dy[way]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            #정상인
            if visited_able[nx][ny] == 0 and flag == 0 and field[nx][ny] == prev:
                visited_able[nx][ny] = 1
                queue.append((field[nx][ny], nx, ny))
            #색약
            if visited_disable[nx][ny] == 0 and flag == 1:
                if field[nx][ny] in ['G', 'R'] and prev in ['G', 'R']:
                    visited_disable[nx][ny] = 1
                    queue.append((field[nx][ny], nx, ny))
                elif field[nx][ny] == prev:
                    visited_disable[nx][ny] = 1
                    queue.append((field[nx][ny], nx, ny))
able_count = 0
disable_count = 0
for i in range(n):
    for j in range(n):
        if visited_able[i][j] == 0:
            bfs(field[i][j], i, j, 0)
            able_count += 1
        if visited_disable[i][j] == 0:
            bfs(field[i][j], i, j, 1)
            disable_count += 1

print(able_count, disable_count)

# bfs 반복 횟수를 구하면 되는 문제
# 적록색맹인 경우 두 색을 같은 것으로 보고 진행하면 됨