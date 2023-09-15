import heapq

m, n = map(int, input().split())
board = [list(str(input())) for _ in range(n)]
pq = []
dist = [[float('inf')]*m for _ in range(n)]
heapq.heappush(pq, (0, 0, 0))
dist[0][0] = 0

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

while pq:
    cx, cy, cnt = heapq.heappop(pq)

    if cnt > dist[cx][cy]:
        continue

    for di in range(4):
        nx, ny = cx + dx[di], cy + dy[di]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if dist[nx][ny] <= cnt + int(board[nx][ny]):
            continue
        heapq.heappush(pq, (nx, ny, cnt + int(board[nx][ny])))
        dist[nx][ny] = cnt + int(board[nx][ny])

print(dist[n-1][m-1])
