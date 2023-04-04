# 모든 경우의 수 탐색으로는 절대 문제 해결 불가
# 시간, 메모리 모두 빡빡한 문제
from collections import deque
N, M = map(int, input().split())
field = [list(map(int, list(input()))) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
min_route = -1
temp = [[[0]*2 for _ in range(M)] for _ in range(N)]
count = 0
queue = deque()
queue.append([0, 0, 0])
temp[0][0][0] = 1
while queue:
    x, y, count = queue.popleft()
    if x == N - 1 and y == M - 1:
        min_route = temp[x][y][count]
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if field[nx][ny] == 1 and count == 0:
            temp[nx][ny][1] = temp[x][y][count] + 1
            queue.append([nx, ny, 1])
        elif field[nx][ny] == 0 and temp[nx][ny][count] == 0:
            temp[nx][ny][count] = temp[x][y][count] + 1
            queue.append([nx, ny, count])
for i in range(N):
    print(temp[i])
print(min_route)