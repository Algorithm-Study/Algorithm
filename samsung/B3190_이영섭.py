from collections import deque

N = int(input())
K = int(input())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

dq = deque()
snake = deque()
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x, y = input().split()
    board[int(x)-1][int(y)-1] = 1
L = int(input())
for _ in range(L):
    num, cdir = input().split()
    dq.append((int(num), cdir))
cnt = 0
dir = 2
snake.append((0, 0))
nx, ny = 0, 1
snake.append((nx, ny))
while True:
    cnt += 1
    nx += dx[dir]
    ny += dy[dir]
    
    if nx < 0 or nx >= N or ny < 0 or ny >= N: break
    if (nx, ny) in snake:
        break
    elif board[nx][ny] == 1:
        snake.append((nx, ny))
        board[nx][ny] = 0
    elif board[nx][ny] == 0:
        snake.append((nx, ny))
        snake.popleft()
    
    if dq and cnt == dq[0][0]:
        dis, cdir = dq.popleft()
        if cdir == 'L':
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4
    
print(cnt)

# 문제 풀이 방법
# # 