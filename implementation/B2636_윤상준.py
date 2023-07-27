import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
 
n, m = map(int, input().split())
cheeze = []
count = 0
#입릭 몇 처음 치즈 갯수 계산
for i in range(n):
    cheeze.append(list(map(int, input().split())))
    count += sum(cheeze[i])
time = 1
while True:
    visited = [[0] * m for _ in range(n)]
    queue = deque([(0, 0)])
    melt = deque([])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            if cheeze[nx][ny] == 0: 
                queue.append((nx, ny))
            elif cheeze[nx][ny] == 1:  
                melt.append((nx, ny))
    # 녹는 치즈 삭제
    for x, y in melt:
        cheeze[x][y] = 0 
    before = len(melt)
    count -= before
    # 다 녹아버린 경우
    if count == 0:  
        print(time)
        print(before)
        break
    time += 1

# 치즈가 외곽에는 존재할 수 없어서 쉽게 확인할 수 있었던 문제