from collections import deque
k = int(input())
m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dq = deque()
# for _ in maps:
#     print(*_)
    
dq.append((0,0,0))
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
# for _ in visited:
#     print(*_)

dx1 = [0, 0, -1, 1]
dy1 = [1, -1, 0, 0]
dx2 = [-2, -1, 1, 2, 2, 1, -1, -2]
dy2 = [ 1, 2, 2, 1, -1, -2, -2, -1]
while dq:
    x, y, z = dq.popleft()
    if x == n-1 and y == m-1:
        print(visited[x][y][z])
        exit()
    for idx in range(4):
        nx = x + dx1[idx]
        ny = y + dy1[idx]
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                dq.append([nx, ny, z])
    if z < k:
        for idx in range(8):
            nx = x + dx2[idx]
            ny = y + dy2[idx]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0 and visited[nx][ny][z+1] == 0:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    dq.append([nx, ny, z+1])
                
print(-1)

'''
1
3 3
0 1 0
1 1 0
0 0 0
>> 2

4
4 4
0 0 1 1
1 0 0 1
1 0 0 1
1 1 0 0
>> 2

1
3 1
0 0 0
>> 2

1
1 1
0
>> 0

1
4 4
0 0 0 0
0 0 0 0
0 0 1 1
0 0 1 0
>> 4
'''