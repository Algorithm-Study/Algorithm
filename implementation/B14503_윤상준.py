n, m = map(int,input().split())
r, c, d = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
field = [list(map(int, input().split())) for _ in range(n)]
count = 0
if field[r][c] == 0:
    field[r][c] = -1
    count -= 1
if d == 1:
    origin = 3
elif d == 3:
    origin = 1
else:
    origin = d
flag = 0
i = 1
while True:
    #for f in field:
    #    print(f)
    #print(f'=========={i}=========={origin}') 
    # 한바퀴 돌면서 청소 안한 곳 체크
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx < 0 or ny < 0 or nx>=n or ny >=m:
            continue
        if field[nx][ny] == 0:
            flag = 1
    # 공간이 없는 경우 -> 후진
    if flag == 0:
        nx = r - dx[origin]
        ny = c - dy[origin]
        if nx < 0 or ny < 0 or nx>=n or ny >=m or field[nx][ny] == 1:
            print(-count)
            break
        else:
            r, c =  nx, ny
    # 빈 공간이 있는 경우 -> 회전후 전진
    else:
        for i in range(1,5):
            check = (origin + i)%4
            nx = r + dx[check]
            ny = c + dy[check]
            if field[nx][ny] == 0:
                count -= 1
                field[nx][ny] = count
                flag = 0
                origin = check
                r, c = nx, ny
                break

    i+=1
    