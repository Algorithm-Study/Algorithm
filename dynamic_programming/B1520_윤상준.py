from collections import deque
m, n = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1]*n for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(start):
    x, y = start
    if x == m-1 and y == n-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if field[nx][ny] < field[x][y]:
           count += dfs([nx,ny])
    visited[x][y] = count
    return visited[x][y]
print(dfs([0,0]))
# 500 X 500의 이동영역을 계산은 시간 초과 발생
# 시간을 줄이기 위해서 DP를 적용해서 문제 풀이를 진행해야 함
# visited를 0으로 초기화한 경우 해당 0인 경우에 대한 처리가 되지 않아서 시간 초과 발생