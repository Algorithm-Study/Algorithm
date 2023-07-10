from itertools import combinations
from collections import deque

arr = [list(input()) for _ in range(5)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
answer = 0

for case in combinations(range(25),7):
    visited = [[False]*5 for _ in range(5)]
    q = deque()
    position = []
    
    cnt = 0
    for c in case:
        x, y = c//5, c%5
        position.append((x, y))
        if arr[x][y] == 'S':
            cnt += 1
            
    if cnt <= 3:
        continue

    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()      
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False and (nx, ny) in position:
                visited[nx][ny] = True
                q.append((nx, ny))
                
    for x, y in position:
        if visited[x][y] == False:
            break
    else:
        answer += 1
        
print(answer)