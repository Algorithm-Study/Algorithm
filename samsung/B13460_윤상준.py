# 구슬 두개의 위치 파악하기
from collections import deque
n, m = map(int,input().split())
queue = deque()
field = []
visited = []
for i in range(n):
    line = list(input())
    if 'R' in line:
        r_start = [i, line.index('R')]
    if 'B' in line:
        b_start = [i, line.index('B')]
    field.append(line)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
field[r_start[0]][r_start[1]], field[b_start[0]][b_start[1]] = '.','.'
queue.append([0, r_start[0], r_start[1], b_start[0], b_start[1]])
visited.append([r_start[0], r_start[1], b_start[0], b_start[1]])
def labyrinth(): 
    while queue:
        move, redx, redy, bluex, bluey = queue.popleft()
        for i in range(4):
            rednx, redny, bluenx, blueny = redx, redy, bluex, bluey
            while field[bluenx + dx[i]][blueny + dy[i]] == '.':
                bluenx += dx[i]
                blueny += dy[i]
            if field[bluenx + dx[i]][blueny + dy[i]] == 'O':
                continue
            while field[rednx + dx[i]][redny + dy[i]] == '.':
                rednx += dx[i]
                redny += dy[i]
            if field[rednx + dx[i]][redny + dy[i]] == 'O':
                return move + 1
            else:
                if rednx == bluenx and redny == blueny:
                    if abs(redx - rednx) + abs(redy - redny) > abs(bluex - bluenx) + abs(bluey - blueny):
                        rednx -= dx[i]
                        redny -= dy[i]
                    else:
                        bluenx -= dx[i]
                        blueny -= dy[i]

                if [rednx, redny, bluenx, blueny] not in visited:
                    queue.append([move +1, rednx, redny, bluenx, blueny])
                    visited.append([rednx, redny, bluenx, blueny])
        if move + 1 > 10:
            return -1
    return -1
print(labyrinth())
             