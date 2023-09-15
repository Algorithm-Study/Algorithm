import heapq
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
m, n = map(int, input().split())
field = []
for _ in range(n):
    line = [int(x) for x in list(input())]
    field.append(line)
# 벽을 부순 횟수, x,y
queue = [(0,0,0)]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
while queue:
    cnt, x, y = heapq.heappop(queue)
    if x == n-1 and y == m-1:
        print(cnt)
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        if field[nx][ny] == 1:
            visited[nx][ny] = 1
            heapq.heappush(queue, (cnt+1,nx,ny))
        else:
            heapq.heappush(queue, (cnt,nx,ny))
print(0)  