R, C, M = map(int, input().split())
maps = [[0]*C for _ in range(R)]
sharks = []

for _ in range(M):
    tmp = list(map(int,input().split()))
    sharks.append(tmp)
    maps[tmp[0]-1][tmp[1]-1] = _+1
    
print('_'*C)
for _ in maps:
    print(*_)

print(sharks)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
for j in range(C):
    

    temp = []
    for i, shark in enumerate(sharks):
        x, y, s, d, h = shark
        if d == 3:
            if y + s - 1 >= C:
                nx = x
                ny = 2*(C - 1) - (y + s - 1)
                d = 4
            else:
                nx = x - 1
                ny = y + s - 1
                d = 4
                
        elif d == 4:
            if y - s - 1 < 0:
                nx = x - 1
                ny = -(y - s - 1)
                d = 3
            else:
                nx = x - 1
                ny = y - s - 1
                d = 3
        
        elif d == 2:
            if x + s -1 >= R:
                nx = 2*(R - 1) - (x + s - 1)
                ny = y -1
                d = 1
            else:
                nx = (x + s - 1)
                ny = y -1
                d = 1
        
        elif d == 1:
            if x - s -1 < 0:
                nx = -(x - s - 1)
                ny = y -1
                d = 2
            else:
                nx = (x + s - 1)
                ny = y -1
                d = 1
        print(nx, ny)        
        if maps[nx][ny] == 0:
            maps[nx][ny] == i + 1
        else:
            if sharks[i][4] > sharks[maps[nx][ny]+1][4]:
                maps[nx][ny] = i + 1
            else:
                del sharks[i]


    
    for i in range(R):
        if maps[i][j] != 0:
            answer += maps[i][j]
            del shark[maps[i][j]]
            maps[i][j] = 0
    print('-'*2*C)
    for _ in maps:
        print(*_)