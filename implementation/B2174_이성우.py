c, r = map(int, input().split())
n, m = map(int, input().split())
robots = list()
for _ in range(n):
    y, x, d = input().split()
    robots.append([r-int(x), int(y)-1, d])
commands = list()
for _ in range(m):
    num, command, itr = input().split()
    commands.append((int(num), command, int(itr)))

arr = [[0 for _ in range(c)] for _ in range(r)]
for idx, robot in enumerate(robots):
    x, y, d = robot
    arr[x][y] = idx+1
    
direction = {'N':(-1, 0), 'W':(0, -1), 'S':(1, 0), 'E':(0, 1)}
angle = ['N', 'E', 'S', 'W']

for num, command, itr in commands:
    for _ in range(itr):
        x, y, d = robots[num-1]
        if command == 'F':
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            if not(0 <= nx < r and 0 <= ny < c):
                print(f'Robot {num} crashes into the wall')
                exit()
                
            if arr[nx][ny] != 0:
                print(f'Robot {num} crashes into robot {arr[nx][ny]}')
                exit()
        else:
            nx = x
            ny = y
            RL = {'R':1, 'L':-1}
            d = angle[(angle.index(d)+RL[command])%4]

        robots[num-1] = [nx, ny, d]
        arr[x][y] = 0
        arr[nx][ny] = num
print('OK')
