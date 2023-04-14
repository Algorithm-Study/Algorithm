from collections import deque

n, m = map(int, input().split())
arr = [0]*101
visited = [False]*101

snake = {}
ladder = {}
for _ in range(n):
    i,j = map(int, input().split())
    ladder[i] = j

for _ in range(m):
    i,j = map(int,input().split())
    snake[i] = j

def bfs():
    dq = deque([1])
    visited[1] = True
    while dq:
        x = dq.popleft()
        for dx in range(1,7):
            nx = x + dx
            if 0 < nx <= 100 and not visited[nx]:
                if nx in ladder:
                    nx = ladder[nx]
                
                if nx in snake:
                    nx = snake[nx]
                    
                if not visited[nx]:
                    dq.append(nx)
                    visited[nx] = True
                    arr[nx] = arr[x] + 1

bfs()
print(arr[100])