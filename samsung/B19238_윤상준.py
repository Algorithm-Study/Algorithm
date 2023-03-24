import sys
import copy
from collections import deque
input = sys.stdin.readline
n, customer, fuel = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
start = [x-1 for x in list(map(int,input().split()))]
pos = []
des = []
for _ in range(customer):
    x1, y1, x2, y2 = map(int, input().split())
    pos.append([x1-1, y1-1])
    des.append([x2-1, y2-1])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(start, goal):
    if start in goal:
        return [-1]
    temp = copy.deepcopy(field)
    temp[start[0]][start[1]] = 1
    queue = deque()
    queue.append([0, start[0], start[1]])
    while queue:
        #print('='*20)
        #print(queue)
        count, x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny < 0 or nx>=n or ny>=n:
                continue
            if temp[nx][ny] == 0:
                temp[nx][ny] = -(count+1)
                queue.append([count + 1,nx, ny])
    return [-temp[x[0]][x[1]] for x in goal]
skip = []
for i in range(customer):
    choice = []
    # 손님까지의 거리 구하기
    choice = bfs(start, pos)
    #print(choice)
    #조건 체크
    if min(choice) == 0 or fuel - min(choice) <0:
        print(-1)
        exit()
    if min(choice) != -1:
        fuel -= min(choice)
    #승객 고르기
    least = min(choice)
    select_list = []
    if len(pos) != len(choice):
        drive = pos.index(start)
    else:
        for j in range(len(choice)):
            select_list.append([j, choice[j], pos[j][0], pos[j][1]])
        select_list.sort(key = lambda x:(x[1], x[2], x[3]))
        for sel in select_list:
            if sel[1] == least:
                drive = sel[0]
                break
    new_start = pos[drive]
    #도착거리 구하기
    to_goal = bfs(new_start, [des[drive]])
    if to_goal == [0]:
        print(-1)
        exit()
    if fuel - to_goal[0] < 0:
        print(-1)
        exit()
    fuel += to_goal[0]
    start = des[drive]
    pos.pop(drive)
    des.pop(drive)
print(fuel)
#bfs n번 진행시 시간초과
# 테케 모음: https://www.acmicpc.net/board/view/58112
# 예외 케이스 및 세부 조건 충족해야 함