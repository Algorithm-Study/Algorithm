import heapq

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
pq = [(0, 0, 0)]
visit = [[float('inf')]*N for _ in range(N)]
visit[0][0] = 0

while pq:
    cx, cy, cv = heapq.heappop(pq)
    if visit[cx][cy] < cv:
        continue
    for di in range(4):
        nx, ny = cx + dx[di], cy + dy[di]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        nv = max(cv, abs(board[cx][cy] - board[nx][ny]))
        if visit[nx][ny] > nv:
            visit[nx][ny] = nv
            heapq.heappush(pq, (nx, ny, nv))

print(visit[N-1][N-1])
