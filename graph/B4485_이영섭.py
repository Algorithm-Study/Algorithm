import heapq

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

problem_number = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    dist = [[float('INF')]*N for _ in range(N)]
    pq = []
    heapq.heappush(pq, (board[0][0], 0, 0))
    dist[0][0] = 0

    while pq:
        cost, x, y = heapq.heappop(pq)
        if x == N - 1 and y == N - 1:
            print(f"Problem {problem_number}: {dist[x][y]}")
            break
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            n_cost = cost + board[nx][ny]
            if n_cost < dist[nx][ny]:
                dist[nx][ny] = n_cost
                heapq.heappush(pq, (n_cost, nx, ny))
    problem_number += 1

