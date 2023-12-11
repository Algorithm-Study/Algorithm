import heapq
n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
queue = []
# -1 : 도로 건설 불가, 0: 이미 건설된 상태, 1: 1의 비용이 필요, 2: 2의 비용이 필요
if field[0][0] == -1:
    print(-1)
    exit()
else:
    heapq.heappush(queue,(field[0][0], 0, 0))
visited[0][0] = 1
while queue:
    cost, x, y = heapq.heappop(queue)
    if x == n-1 and y == m-1:
        print(cost)
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >=m or visited[nx][ny] or field[nx][ny] == -1:
            continue
        visited[nx][ny] = 1
        heapq.heappush(queue,(cost + field[nx][ny], nx, ny))
print(-1)