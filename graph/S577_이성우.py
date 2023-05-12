import sys
from collections import deque

def check(x, y):
    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] == '#':
            start = directions[i]
            cnt += 1

    if cnt > 1:
        return False

    return start


def bfs(i, j):
    path = deque([])
    queue = deque([[i,j]])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            direction = directions[i]
            
            if 0 <= nx < H and 0 <= ny < W:
                if maps[nx][ny] == '#' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    path.append(direction)
                    queue.append([nx,ny])
                    

    return path


H, W = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
visited = [[False] * W for _ in range(H)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
directions = ['^','>','v','<']
ans = []

for row in range(H):       
    for col in range(W):
        if maps[row][col] == '#' and check(row, col):
            path = bfs(row, col)
            print(row+1, col+1)
            print(path[0])
           
            current = path.popleft()
            
            cnt = 1
            for next in path:
                if current == next:
                    cnt += 1
                    current = next
                    
                    if cnt % 2 == 0:
                        ans.append("A")
                        cnt = 0
                        
                else:
	                # index가 감소 됐을 때 일치한다 -> 왼쪽으로 회전
                    if directions[directions.index(current) - 1] == next:
                        ans.append("L")
                            
                    else:
	                    # index가 증가 됐을 때 일치한다 -> 오른쪽으로 회전
                        ans.append("R")
                    
                    current = next
                    cnt = 1
                    
            for i in ans:
                print(i, end="")  
                    
            sys.exit()