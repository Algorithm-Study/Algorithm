import heapq
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
field = [[0]*501 for _ in range(501)]
visited = [[0]*501 for _ in range(501)]
# 위험 구역 설정
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(501):
        for j in range(501):
            if min(x1,x2) <= i <= max(x1,x2) and min(y1,y2) <= j <= max(y1,y2):
                field[i][j] = 1
# 죽음 구역 설정
m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(501):
        for j in range(501):
            if min(x1,x2) <= i <= max(x1,x2) and min(y1,y2) <= j <= max(y1,y2):
                field[i][j] = 2
#감소 생명, x, y
queue = [(0,0,0)]
visited[0][0] = 1
while queue:
    life, x, y = heapq.heappop(queue)
    if x == 500 and y == 500:
        print(life)
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx > 500 or ny > 500 or visited[nx][ny]:
            continue
        if field[nx][ny] == 1:
            heapq.heappush(queue,(life + 1, nx, ny))
            visited[nx][ny] = 1
        elif field[nx][ny] == 0:
            heapq.heappush(queue,(life, nx, ny))
            visited[nx][ny] = 1
print(-1)
# 우선순위 큐로 생명이 최소로 감소된 경우가 먼저 진행되도록 설정