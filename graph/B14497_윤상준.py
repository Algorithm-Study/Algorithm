import sys
import heapq
dx = [-1,0,1,0]
dy = [0,-1,0,1]
INF = sys.maxsize
n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
field = [list(input()) for _ in range(n)]
distance = [[INF]*m for _ in range(n)]

distance[x1-1][y1-1] = 1
queue = []
heapq.heappush(queue,[1,x1-1,y1-1])
while queue:
    cost, x, y = heapq.heappop(queue)
    if distance[x][y] < cost:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if field[nx][ny] == '0' and distance[nx][ny] > cost:
            heapq.heappush(queue, [cost, nx, ny])
            distance[nx][ny] = cost
        elif field[nx][ny] == '1' and distance[nx][ny] > cost + 1:
            heapq.heappush(queue, [cost+1, nx, ny])
            distance[nx][ny] = cost + 1
        elif field[nx][ny] == '#':
            print(cost)
            exit()
