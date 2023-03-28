from itertools import combinations
from collections import deque
from copy import deepcopy
n, m = map(int, input().split())
field = []
possible = []
cnt = 0
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            possible.append([i,j])
            temp[j] = 0
            cnt +=1
        if temp[j] == 1:
            cnt +=1
    field.append(temp)
choices = list(combinations(possible, m))
queue = deque()
dx = [-1, 0, 1, 0 ]
dy = [0, 1, 0, -1 ]
time_list = []
def bfs(field, vacant):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >=n or field[nx][ny] == 1:
                continue
            if vacant == 0:
                    break
            if [nx,ny] in possible and field[nx][ny] == 0:
                field[nx][ny] = field[x][y] - 1
                queue.append([nx,ny])
            if field[nx][ny] == 0:
                field[nx][ny] = field[x][y] - 1
                queue.append([nx,ny])
                vacant -= 1
    #for i in range(n):
    #    print(field[i])
    #print(-(min([min(x) for x in field])+1) )
    #print('='*20)
    for i in range(n):
        if 0 in field[i] and vacant != 0:
            return -1
    return -(min([min(x) for x in field])+1) 
for choice in choices:
    t_field = deepcopy(field)
    for c in choice:
        queue.append(c)
        t_field[c[0]][c[1]] = -1
    vacant = n**2 - cnt
    #print(vacant)
    time_list.append(bfs(t_field, vacant))
time_list = [x for x in time_list if x>-1]
if len(time_list) == 0:
    print(-1)
else:
    print(min(time_list))