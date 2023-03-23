n, m = map(int,input().split())
field = [list(map(int,input().split())) for i in range(n)]
moves = []
for i in range(m):
    way, count = map(int,input().split())
    moves.append([way-1,count])
cloud = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
bugx = [-1, -1, 1, 1]
bugy = [-1, 1, -1, 1]
for move in moves:
    way, count = move
    forecast = []
    for c in cloud:
        nx = (c[0] + dx[way] * count) % n
        ny = (c[1] + dy[way] * count) % n
        forecast.append([nx,ny])
    visited = [[0]*n for _ in range(n)]
    cloud = []
    for f in forecast:
        field[f[0]][f[1]] += 1
        visited[f[0]][f[1]] = 1
    for x,y in forecast:
        bug = 0
        for i in range(4):
            nx = x + bugx[i]
            ny = y + bugy[i]
            if 0<= nx <n and 0<= ny <n and field[nx][ny] != 0:
                bug +=1
        field[x][y] += bug
    for i in range(n):
        for j in range(n):
            if field[i][j] >= 2 and visited[i][j] == 0:
                field[i][j] -= 2
                cloud.append([i,j])

answer = sum([sum(x) for x in field])
#print(field)
print(answer)