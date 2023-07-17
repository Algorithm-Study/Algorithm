from collections import deque
n, m = map(int, input().split())
field = []
way = {'U': (-1,0), 'D': (1,0), 'L': (0,-1),'R': (0,1)}
parent = [x for x in range(n*m+1)]
visited = [[0]*m for _ in range(n)]

for _ in range(n):
    field.append(list(input()))

count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            record = [(i,j)]
            queue = deque()
            queue.append((i,j))
            visited[i][j] = 1
            while queue:
                x,y = queue.popleft()
                dx, dy = way[field[x][y]]
                nx, ny = x + dx, y + dy
                if visited[nx][ny]:
                    if (nx,ny) in record:
                        count += 1
                        break
                    else:
                        break
                visited[nx][ny] = 1
                queue.append((nx,ny))
                record.append((nx,ny))
print(count)
# 사이클을 계속 돌다가 재방문한 경우 이번에 방문한 것인지 아닌지 체크
# 이를 통해 안전 영역 수를 계산