import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()

# 초기 토마토 저장
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j])

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 탐색
while q:
    x, y = q.popleft()
    
    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            # 안익었으면 이전 값 +1로 익은 거 확인
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])

answer = 0
for line in arr:
    if 0 in line:
        print(-1)
        exit()
    answer = max(answer, *line)
print(answer-1)