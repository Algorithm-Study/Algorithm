# 뱀을 사용해야 빠르게 도착할 수 있는 경우가 있는 것으로 보임
# 뱀 뱀 뱀 뱀 뱀 뱀 사다리 뱀 뱀 뱀 뱀 뱀 뱀 . . . . . . . 뱀 . . . . . . . . . . . .사다리 도착지점
from collections import deque
board = [0 for x in range(1,101)]
visited = [0 for x in range(1,101)]
n, m = map(int, input().split())
# 뱀 과 사다리 삽입
for i in range(n+m):
    start, goal = map(int, input().split())
    board[start-1] = goal - 1
queue = deque()
queue.append([0,0])
visited[0] = 1
while queue:
    pos, count = queue.popleft()
    if pos == 99:
        print(count)
        break
    for i in range(1,7):
        nx = pos + i
        if nx >= 100:
            continue
        #뱀에 도착한 경우
        if board[nx] > 0 and visited[nx] == 0:
            visited[nx] = 1
            visited[board[nx]] = 1
            queue.append([board[nx], count+1])
        #사다리에 도착한 경우
        elif board[nx] > 0 and visited[nx] == 0:
            visited[nx] = 1
            visited[board[nx]] = 1
            queue.append([board[nx], count+1])
        elif visited[nx] == 0:
            visited[nx] = 1
            queue.append([nx, count+1])