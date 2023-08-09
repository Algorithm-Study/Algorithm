from collections import deque
ways = [(-1,0),(0,-1),(1,0),(0,1)]
n, m = map(int, input().split())
field = []
cheese = 0
for _ in range(n):
    line = list(map(int, input().split()))
    cheese += sum(line)
    field.append(line)
count = 0
while cheese:
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append((0,0))
    melt = []
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + ways[i][0]
            ny = y + ways[i][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 치즈에 방문한 경우
            if field[nx][ny] == 1:
                visited[nx][ny] += 1
                if visited[nx][ny] == 2:
                    melt.append((nx,ny))
            # 공기인 경우
            else:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    # 녹는 치즈 처리
    cheese -= len(melt)
    for x,y in melt:
        field[x][y] = 0
    count += 1
print(count)
# BFS를 실행해서 공기와 마주친 곳이 2개 이상이면 없어지도록 구현하면 끝