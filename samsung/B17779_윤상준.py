from collections import deque
n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
total = sum([sum(x) for x in field])
result = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for x in range(n):
    for y in range(n):
        for d1 in range(1,n-1):
            for d2 in range(1,n-1):
                # 진행할 수 없는 조건
                if d1+d2+x >= n or y - d1 < 0 or y + d2 >= n:
                    continue 
                # 경계 칠하기
                boundary = [[0]* n for _ in range(n)]
                for x1, y1 in zip(range(x,x+d1+1),range(y,y-d1-1, -1)):
                        boundary[x1][y1] = 1
                for x1, y1 in zip(range(x,x+d2+1), range(y,y+d2+1)):
                        boundary[x1][y1] = 1
                for x1, y1 in zip(range(x+d1,x+d1+d2+1), range(y-d1,y-d1+d2+1)):
                        boundary[x1][y1] = 1
                for x1, y1 in zip(range(x+d2,x+d2+d1+1), range(y+d2,y+d2-d1-1, -1)):
                        boundary[x1][y1] = 1
                # 인구 구하기
                population = []
                queue = deque()
                queue.append((0,0))
                temp = field[0][0]
                boundary[0][0] = 2
                while queue:
                    x2,y2 = queue.popleft()
                    for i in range(4):
                        nx = x2 + dx[i]
                        ny = y2 + dy[i]
                        if nx < 0 or nx >= x + d1 or ny < 0 or ny > y or boundary[nx][ny] != 0:
                            continue
                        temp += field[nx][ny]
                        boundary[nx][ny] = 2
                        queue.append((nx,ny))
                population.append(temp)
                queue.append((0,n-1))
                temp = field[0][n-1]
                boundary[0][n-1] = 2
                while queue:
                    x2,y2 = queue.popleft()
                    for i in range(4):
                        nx = x2 + dx[i]
                        ny = y2 + dy[i]
                        if nx < 0 or nx > x + d2 or ny <= y or ny >= n or boundary[nx][ny] != 0:
                            continue
                        temp += field[nx][ny]
                        boundary[nx][ny] = 2
                        queue.append((nx,ny))
                population.append(temp)
                queue.append((n-1,0))
                temp = field[n-1][0]
                boundary[n-1][0] = 2
                while queue:
                    x2,y2 = queue.popleft()
                    for i in range(4):
                        nx = x2 + dx[i]
                        ny = y2 + dy[i]
                        if nx < x+d1 or nx >= n or ny < 0 or ny >= y -d1 + d2 or boundary[nx][ny] != 0:
                            continue
                        temp += field[nx][ny]
                        boundary[nx][ny] = 2
                        queue.append((nx,ny))
                population.append(temp)
                queue.append((n-1,n-1))
                temp = field[n-1][n-1]
                boundary[n-1][n-1] = 2
                while queue:
                    x2,y2 = queue.popleft()
                    for i in range(4):
                        nx = x2 + dx[i]
                        ny = y2 + dy[i]
                        if nx <= x+d2 or nx >= n or ny < y-d1+d2 or ny >= n or boundary[nx][ny] != 0:
                            continue
                        temp += field[nx][ny]
                        boundary[nx][ny] = 2
                        queue.append((nx,ny))
                population.append(temp)
                population.append(total -sum(population))
                result.append(max(population)-min(population))
print(min(result))
# 조건에 맞게 구현하면 되는 문제
# 5구역은 바운더리만 계산해서 bfs로 나머지 구역 검출
# 조건을 리스트화 하면 반복되는 코드 줄일 수 있을 것으로 예상