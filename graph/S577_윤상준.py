import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())
field = [list(input().rstrip()) for _ in range(a)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
directions = ['^', '<', 'v', '>']
visited = [[0]*b for _ in range(a)]
method = []
# 직접 시작 시점을 찾아야 함
def find_startpoint(x,y):
    connected = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= a or ny >= b or field[nx][ny] != '#':
            continue
        startway = directions[i]
        connected += 1
    if connected > 1:
        return False
    else:
        return True

for i in range(a):
    for j in range(b):
        if field[i][j] == '#' and find_startpoint(i,j):
            queue = deque()
            visited[i][j] = 1
            record = []
            queue.append([i,j])
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    direction = directions[k]
                    if nx < 0 or ny < 0 or nx >= a or ny >= b or field[nx][ny] != '#' or visited[nx][ny] == 1:
                        continue
                    visited[nx][ny] = 1
                    record.append(direction)
                    queue.append([nx, ny])
            record = deque(record)
            print(i+1, j+1)
            print(record[0])
            status = record.popleft()
            count = 1
            for r in record:
                if status == r:
                    count += 1
                    status = r
                    if count % 2 == 0:
                        method.append('A')
                        count = 0
                else:
                    if directions[directions.index(status) - 1] == r:
                        method.append('R')
                    else:
                        method.append('L')
                    status = r
                    count = 1
            print("".join(method))
            sys.exit(0)
# 한번에 2씩 이동, 갔단 곳에 방문하지 않은 이유 -> 시작 위치 추정이 가능하게 하기 위함
# 테케 다 맞을 필요가 없음 -> 처음과 끝이 뒤바뀐 경우 답이 바뀔 수 밖에 없음
# 일단 bfs로 탐색한 다음 2번 이동하면 A를 추가하는 방식으로 코드를 진행하면 됨
# 조건이 너무 많아서 나누어서 문제를 풀어야 함
         


            

