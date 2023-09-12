from itertools import permutations
from collections import deque
answer = 50*100 + 1
n,m,k = map(int, input().split())
initial = [list(map(int, input().split())) for _ in range(n)]
rotates = [list(map(int, input().split())) for _ in range(k)]
def rotation(x,y,height,width):
    queue = deque()
    # 윗변 데이터 추가
    for i in range(y, y+width):
        queue.append(field[x][i])
    # 오른쪽 변 데이터 추가
    for i in range(x+1,x+height):
        queue.append(field[i][y+width-1])
    # 아래쪽 변 데이터 추가
    for i in range(y+width-2, y-1, -1):
        queue.append(field[x+height-1][i])
    # 왼쪽 변 데이터 추가
    for i in range(x+height-2,x, -1):
        queue.append(field[i][y])
    queue.rotate(1)
    # 회전 후 데이터 추가(위->오->아래->왼쪽)
    for i in range(y, y+width):
        field[x][i] = queue.popleft()
    for i in range(x+1,x+height):
        field[i][y+width-1] = queue.popleft()
    for i in range(y+width-2, y-1, -1):
        field[x+height-1][i] = queue.popleft()
    for i in range(x+height-2,x, -1):
        field[i][y] = queue.popleft()
for case in permutations(rotates,k):
    field = [x[:] for x in initial]
    for r,c,s in case:
        lx,ly = r-s-1, c-s-1
        height, width = 2*s+1, 2*s+1
        while height > 0 and width > 0:
            rotation(lx, ly, height,width)
            lx, ly = lx + 1, ly + 1
            height, width = height - 2, width -2
    for i in range(n):
        answer = min(answer, sum(field[i]))
print(answer)