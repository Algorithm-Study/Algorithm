from collections import deque
field = [list(input()) for _ in range(12)]
ways = [(-1, 0), (0, -1), (1, 0), (0, 1)]
streak = 0
while True:
    visited = [[0]*6 for _ in range(12)]
    erase = []
    # 뿌요뿌요 조건에 맞는지 체크
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and field[i][j] != '.':
                queue = deque()
                queue.append((i,j))
                count = 1
                record = [(i,j)]
                visited[i][j] = 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x+ ways[k][0]
                        ny = y+ ways[k][1]
                        if nx < 0 or ny < 0 or nx >= 12 or ny >= 6 or visited[nx][ny] == 1:
                            continue
                        if field[x][y] == field[nx][ny]:
                            visited[nx][ny] = 1
                            queue.append((nx,ny))
                            record.append((nx,ny))
                            count += 1
                if count >= 4:
                    erase = erase + record
    #제거 할 것이 없는 경우
    if not erase:
        break
    # 뿌요뿌요 삭제
    for x,y in erase:
        field[x][y] = '.'
    # 뿌요뿌요 내려오기
    for i in range(6):
        line = [x[i] for x in field if x[i] != '.' ]
        line = ['.']*(12-len(line)) + line
        for j in range(12):
            field[j][i] = line[j]
    streak += 1
print(streak)