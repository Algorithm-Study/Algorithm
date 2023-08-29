def make_tmp(i):
    for x in range(n):
        for y in range(n):
            if position[x][y] and position[x][y][0][0] == i:
                tmp = position[x][y][:]
                position[x][y] = []
                return x, y, tmp
                
def move(x, y, tmp, check):
    nx = x + dx[tmp[0][1]]
    ny = y + dy[tmp[0][1]]
    if 0 <= nx < n and 0 <= ny < n:
        if arr[nx][ny] == 0:
            position[nx][ny].extend(tmp)
        elif arr[nx][ny] == 1:
            position[nx][ny].extend(tmp[::-1])
        elif arr[nx][ny] == 2 and check == 0:
            tmp[0][1] = dr[tmp[0][1]]
            move(x, y, tmp, 1)
        else:
            position[x][y].extend(tmp)
    else:
        if check == 0:
            tmp[0][1] = dr[tmp[0][1]]
            move(x, y, tmp, 1)
        else:
            position[x][y].extend(tmp)

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

position = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    x, y, d = map(int, input().split())
    position[x-1][y-1].append([i, d-1])
    
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dr = [1, 0, 3, 2]

answer = 0
while answer <= 1000:
    answer += 1
    for i in range(k):
        result = make_tmp(i)
        if result != None:
            x, y, tmp = result
            move(x, y, tmp, 0)
        
    for x in range(n):
        for y in range(n):
            if len(position[x][y]) >= 4:
                print(answer)
                exit()
print(-1)