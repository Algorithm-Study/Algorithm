from collections import deque
from itertools import combinations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
art_point = 0
center = n//2

def make_group():
    group = []
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                tmp = []
                tmp.append((i, j))
                visited[i][j] = True
                q = deque()
                q.append((i, j))
                
                while q:
                    x, y = q.popleft()
                    
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and arr[nx][ny] == arr[i][j]:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            tmp.append((nx, ny))
                group.append(tmp)
    
    return group

def get_point(g1, g2):
    point = (len(g1) + len(g2))*arr[g1[0][0]][g1[0][1]]*arr[g2[0][0]][g2[0][1]]
    
    cnt1 = 0
    cnt2 = 0
    
    for p in g1:
        x, y = p
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if (nx, ny) in g2:
                cnt1 += 1
                
    for p in g2:
        x, y = p
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if (nx, ny) in g1:
                cnt2 += 1
                
    point *= max(cnt1, cnt2)
    return point

def plus_rotate():
    
    for i in range(n):
        for j in range(n):
            if i == center:
                tmp_arr[i][j] = arr[j][i]
            if j == center:
                tmp_arr[i][j] = arr[n-j-1][n-i-1]

def square_rotate(x, y, l):

    for i in range(x, x+l):
        for j in range(y, y+l):
            ox, oy = i - x, j - y
            rx, ry = oy, l - ox - 1
            tmp_arr[rx + x][ry + y] = arr[i][j]

for _ in range(4):
    group = make_group()

    for g1, g2 in combinations(group, 2):
        art_point += get_point(g1, g2)
        
    tmp_arr = [[0]*n for _ in range(n)]
    
    plus_rotate()

    square_rotate(0, 0, center)
    square_rotate(0, center+1, center)
    square_rotate(center+1, 0, center)
    square_rotate(center+1, center+1, center)

    for i in range(n):
        for j in range(n):
            arr[i][j] = tmp_arr[i][j]
            
print(art_point)