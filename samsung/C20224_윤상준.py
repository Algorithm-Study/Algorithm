# gx: 성장, dx: 제초
gx = [-1,0,1,0]
gy = [0,-1,0,1]
dx = [-1,-1,1,1]
dy = [-1,1,-1,1]
n,m,K,c = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
dead = [[0]*n for _ in range(n)]
killed = 0
for _ in range(m):
    # 성장
    for i in range(n):
        for j in range(n):
            # 나무가 있는 경우
            if field[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i + gx[k]
                    ny = j + gy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if field[nx][ny] > 0:
                        cnt += 1
                field[i][j] += cnt
    # 번식
    breed = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if field[i][j] > 0:
                cnt = 0
                pos = []
                for k in range(4):
                    nx = i + gx[k]
                    ny = j + gy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or dead[nx][ny] != 0:
                        continue
                    if field[nx][ny] == 0:
                        cnt += 1
                        pos.append((nx,ny))
                for px,py in pos:
                    breed[px][py] += field[i][j]//cnt
    for i in range(n):
        for j in range(n):
            field[i][j] += breed[i][j]
    # 제초 위치 선정
    max_kill = 0
    spread_pos = (-1,-1)
    for i in range(n):
        for j in range(n):
            if field[i][j] > 0:
                temp = field[i][j]
                for k in range(4):
                    for l in range(1, K+1):
                        nx = i + l*dx[k]
                        ny = j + l*dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n or field[nx][ny] <= 0:
                            break
                        temp += field[nx][ny]
                if max_kill < temp:
                    max_kill = temp
                    spread_pos = (i,j)
    #약효 감소
    for i in range(n):
        for j in range(n):
            if dead[i][j] > 0:
                dead[i][j] -= 1
    # 제초약 살포
    killed += max_kill
    field[spread_pos[0]][spread_pos[1]] = 0
    dead[spread_pos[0]][spread_pos[1]] = c
    for k in range(4):
        for l in range(1,K+1):
            nx = spread_pos[0] + l*dx[k]
            ny = spread_pos[1] + l*dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break
            dead[nx][ny] = c
            if field[nx][ny] <= 0:
                break
            field[nx][ny] = 0
            
print(killed)
# 약 40분 소요