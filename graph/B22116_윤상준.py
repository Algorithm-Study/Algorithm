import heapq
import sys
INF = sys.maxsize
n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
distance = [[INF]*n for _ in range(n)]
queue = [(0,0,0)]
dir_x = [-1, 0, 1, 0]
dir_y = [0, -1, 0, 1]
distance[0][0] = 0
while queue:
    cost, x, y = heapq.heappop(queue)
    if distance[x][y] < cost:
        continue
    elif x == n-1 and y == n-1:
        print(distance[n-1][n-1])
        exit()
    for dx, dy in zip(dir_x,dir_y):
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        new_cost = max(cost, abs(field[nx][ny] - field[x][y]))
        if distance[nx][ny] > new_cost:
            distance[nx][ny] = new_cost
            heapq.heappush(queue, (new_cost, nx, ny))