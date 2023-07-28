A, B = map(int, input().split())
N, M = map(int, input().split())

board = [[0]*A for _ in range(B)]
robot = [0]
di = {'N': 0, 'W': 1, 'S': 2, 'E': 3}
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(1, N+1):
    x, y, d = input().split()
    x, y = int(x) - 1, int(y)
    board[B-y][x] = i
    robot.append((B-y, x, di[d]))

operation = []
for _ in range(M):
    robot_num, oper, oper_num = input().split()
    robot_num, oper_num = int(robot_num), int(oper_num)
    if oper == 'F':
        for _ in range(oper_num):
            x, y, d, = robot[robot_num]
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or ny < 0 or nx >= B or ny >= A:
                print(f'Robot {str(robot_num)} crashes into the wall')
                exit()
            if board[nx][ny] != 0:
                print(f'Robot {str(robot_num)} crashes into robot {str(board[nx][ny])}')
                exit()
            board[x][y], board[nx][ny] = 0, robot_num
            robot[robot_num] = (nx, ny, d)
    elif oper == 'L':
        x, y, d = robot[robot_num]
        for _ in range(oper_num):
            d = (d + 1) % 4
        robot[robot_num] = (x, y, d)
    elif oper == 'R':
        x, y, d = robot[robot_num]
        for _ in range(oper_num):
            d = (d + 3) % 4
        robot[robot_num] = (x, y, d)
print('OK')
