from collections import deque
def bfs(where, field, height, width):
    queue = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue.append([0,where[0], where[1]])
    while queue:
        #print('='*20)
        #print(queue)
        count, x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= height or ny >=width:
                continue
            if field[nx][ny] == 'L' or field[nx][ny] == 'E':
                return count + 1
            if field[nx][ny] == 'O':
                field[nx][ny] = 'X'
                queue.append([count + 1, nx, ny])
    return -1
        
def solution(maps):
    lever_field = []
    exit_field = []
    lever = [0,0]
    start = [0,0]
    height = len(maps)
    width = len(maps[0])
    for i in range(len(maps)):
        exit_field.append(list(maps[i]))
        lever_field.append(list(maps[i]))
        if 'S' in exit_field[i]:
            pos = exit_field[i].index('S')
            exit_field[i][pos] = 'O'
            lever_field[i][pos] = 'O'
            start = [i, pos]
        if 'L' in exit_field[i]:
            pos = exit_field[i].index('L')
            exit_field[i][pos] = 'O'
            lever = [i, pos]
        if 'E' in exit_field[i]:
            pos = exit_field[i].index('E')
            lever_field[i][pos] = 'O'
    l_count = bfs(start, lever_field, height, width)
    if l_count == -1:
        return -1
    e_count = bfs(lever, exit_field, height, width)
    if e_count == -1:
        return -1
    return l_count + e_count