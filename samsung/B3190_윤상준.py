# 1: 사과 -1: 뱀
n = int(input())
field = [[0]* n for _ in range(n)]
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
way = 2
apple = int(input())
x, y = 0, 0
snake = [[0,0]]
spend = 0
field[0][0]=2
for _ in range(apple):
    a_x, a_y= map(int, input().split())
    field[a_x -1][a_y -1] = 1
operation = int(input())
op_list = []
for _ in range(operation):
    op_list.append(input().split())
j = 0
second, rotate = op_list[j]
while True:
    spend += 1
    #print(spend)
    nx = x + dx[way]
    ny = y + dy[way]
    # 맵의 끝 혹은 자신과 만난 경
    if nx < 0 or ny < 0 or nx >= n or ny >=n or field[nx][ny] == 2:
        print(spend)
        exit()
    # 사과를 만난 경우
    if field[nx][ny] == 1:
        field[nx][ny] = 2
        snake.append([nx,ny])
    # 사과를 만나지 못한 경우
    else:
        field[nx][ny] = 2
        snake.append([nx,ny])
        t_x, t_y = snake.pop(0)
        field[t_x][t_y] = 0
    x, y = nx, ny
    #for i in range(n):
    #    print(field[i])
    if int(second) == spend:
        if rotate == 'L':
            way = way -1 if way-1 >-1 else 3
        else:
            way = way +1 if way+1 <4 else 0
        if j < len(op_list)-1:
            j += 1
            second, rotate = op_list[j]