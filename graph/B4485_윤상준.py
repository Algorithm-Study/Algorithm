import sys, heapq
INF = sys.maxsize
count = 0
dx, dy= [-1, 0, 1, 0], [0, -1, 0, 1]
while True:
    n = int(input())
    count += 1
    if n == 0:
        break
    field = [list(map(int, input().split())) for _ in range(n)]
    stolen = [[INF] * n for _ in range(n)]
    queue = []
    heapq.heappush(queue,(field[0][0], 0, 0))
    while queue:
       rupee, x, y =  heapq.heappop(queue)
       if x == n-1 and y == n-1:
           print(f'Problem {count}: {stolen[x][y]}')
           break
       for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]
           if nx < 0 or ny < 0 or nx >= n or ny >= n:
               continue
           if rupee + field[nx][ny] < stolen[nx][ny]:
               stolen[nx][ny] = rupee + field[nx][ny]
               heapq.heappush(queue,(stolen[nx][ny], nx, ny))
# 최소 비용을 계산하는 간단한 문제