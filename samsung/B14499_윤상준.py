# python3 31256KB/ 48ms
# pypy3 114328KB /132ms
n, m, x, y, k = map(int, input().split())
# 정면, 위, 뒤, 아래
rotate = [0, 0, 0, 0]
#주사위 좌측, 우측
side = [0,0]
field = [list(map(int, input().split())) for _ in range(n)]
operation = list(map(int, input().split()))
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
for op in operation:
    nx = x + dx[op]
    ny = y + dy[op]
    #이동한 결과 벗어나는 경우 생략
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    # top -> right -> down-> left -> top
    if op == 1:
        side[0], side[1], rotate[1], rotate[3] = rotate[3], rotate[1], side[0], side[1]
    # top -> left -> down-> right -> top
    elif op == 2:
        side[0], side[1], rotate[1], rotate[3] = rotate[1], rotate[3], side[1], side[0]
    # 0 -> 1 -> 2 -> 3 -> 0
    elif op == 3:
        temp = rotate[3]
        for i in range(3, 0, -1):
            rotate[i] = rotate[i-1]
        rotate[0] = temp
    # 3 -> 2 -> 1 -> 0 -> 3
    else:
        temp = rotate[0]
        for i in range(3):
            rotate[i] = rotate[i+1]
        rotate[3] = temp
    if field[nx][ny] != 0:
        rotate[3] = field[nx][ny]
        field[nx][ny] = 0
    else:
        field[nx][ny] = rotate[3]
    x = nx
    y = ny
    #print(rotate)
    print(rotate[1])