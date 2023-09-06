import heapq
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n = int(input())
field = [[int(x) for x in list(input())] for _ in range(n)]
visited = [[0]*n for _ in range(n)]
queue = [(0,0,0)]
visited[0][0] = 1
while queue:
    cnt,x,y = heapq.heappop(queue)
    if (x,y) == (n-1,n-1):
        print(cnt)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        if field[nx][ny] == 0:
            heapq.heappush(queue,(cnt+1, nx, ny))
        else:
            heapq.heappush(queue, (cnt, nx, ny))
