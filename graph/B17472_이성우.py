import sys
from collections import deque
input = sys.stdin.readline

# 초기값 설정
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 섬 분류
def seperate_island(i, j, num):
    q = deque()
    q.append((i, j))
    arr[i][j] = num
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0 and visited[nx][ny] == False:
                arr[nx][ny] = num
                visited[nx][ny] = True
                q.append((nx, ny))

# 가능한 간선 탐색
def get_dist(i, j, now):
    q = deque()
    for idx in range(4):
        q.append((i, j, 0, (dx[idx], dy[idx])))
    while q:
        x, y, cnt, now_dir = q.popleft()
        if arr[x][y] != 0 and arr[x][y] != now:
            if cnt > 2:
                edge.add((cnt-1, now, arr[x][y]))
            continue
        nx, ny = x + now_dir[0], y + now_dir[1]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != now:
            q.append((nx, ny, cnt+1, now_dir))
                
num = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            seperate_island(i, j, num)
            num += 1
            
edge = set()     
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            visited = [[False]*m for _ in range(n)]
            get_dist(i, j, arr[i][j])
            
edge = list(edge)
edge.sort()

# 유니온 파인드
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
        
parent = [_ for _ in range(num)]

answer = 0
tmp = 0

# 최소 비용순으로 유니온 파인드 실행
for cost, x, y in edge:
    if find_parent(x) != find_parent(y):
        tmp += 1
        union(x, y)
        answer += cost

# MST는 간선의 수 = 노드의 수 - 1인 점 활용
# num이 1부터 시작했으므로 tmp != num-2로 확인
if answer == 0 or tmp != num-2:
    print(-1)
else:
    print(answer)