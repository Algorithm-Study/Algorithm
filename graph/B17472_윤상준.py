from collections import deque
n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
island_num = 1
# MST 크루스칼을 위한 union-find 구현
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    pa, pb  = find(a), find(b)
    if pa < pb:
        parents[pb] = parents[pa]
    else:
        parents[pa] = parents[pb]
# 필드에 존재하는 섬을 식별하고 넘버링 부여하기
for i in range(n):
    for j in range(m):
        if field[i][j] and not visited[i][j]:
            queue = deque()
            queue.append((i,j))
            field[i][j] = island_num
            visited[i][j] = 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                        continue
                    if field[nx][ny]:
                        field[nx][ny] = island_num
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
            island_num += 1
edges = set()
# 각 섬으로 이동할 수 있는 경우의 수 구하기(시작 섬, 도착 섬, 거리)
for i in range(n):
    for j in range(m):
        if field[i][j]:
            current = field[i][j]
            visited =  [[0]*m for _ in range(n)]
            queue = deque(())
            # 한 방향으로만 가야하기 때문에 방향 정보가 필요
            for k in range(4):
                # x,y,방향, 이동횟수
                queue.append((i,j,k,0))
            visited[i][j] = 1
            while queue:
                x, y, dir, count = queue.popleft()
                # 시작 섬과 다른 섬에 도착했으며 두 섬이 인접하지 않은 경우
                if field[x][y] not in [0,current]:
                    # 다리 길이가 조건을 충족하는 경우
                    if count > 2:
                        edges.add((count-1,current, field[x][y]))
                    continue
                nx, ny = x + dx[dir], y + dy[dir]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or field[nx][ny] == current:
                    continue
                queue.append((nx,ny,dir, count+1))
edges = sorted(list(edges))
parents = [x for x in range(island_num)]
edge_num, result = 0, 0
# print('='*10)
# for i in range(n):
#     print(*field[i])
for cost, start, end in edges:
    # print(parents)
    if find(start) != find(end):
        edge_num += 1
        union(start,end)
        result += cost
if result == 0 or edge_num != island_num -2:
    print(-1)
else:
    print(result)