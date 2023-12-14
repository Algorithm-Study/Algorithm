import heapq

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
pq = []
visit = [[float('inf')]*n for _ in range(m)]
if board[0][0] != -1:
    visit[0][0] = board[0][0]
    heapq.heappush(pq, (board[0][0], 0, 0))
else:
    print(-1)
    exit()

while pq:
    cv, cx, cy = heapq.heappop(pq)
    if visit[cx][cy] < cv:
        continue
    for di in range(4):
        nx, ny = cx + dx[di], cy + dy[di]
        if nx < 0 or ny < 0 or nx >= m or ny >= n or board[nx][ny] == -1:
            continue
        nv = cv + board[nx][ny]
        if visit[nx][ny] > nv:
            heapq.heappush(pq, (nv, nx, ny))
            visit[nx][ny] = nv
if visit[m-1][n-1] == float('inf'):
    print(-1)
else:
    print(visit[m-1][n-1])