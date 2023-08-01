from collections import deque
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
n = int(input())
field = []
# 입력 및 상어 위치 확인
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 9:
            shark_pos = (i, j)
    field.append(line)
time = 0
# 상어 크기, 먹은 먹이
shark_info = [2,0]
while True:
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append(shark_pos)
    visited[shark_pos[0]][shark_pos[1]] = 1
    choices = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖 or 이미 방문한 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] != 0:
                continue
            # 작은 물고기인 경우
            if shark_info[0] > field[nx][ny] and field[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                choices.append((visited[nx][ny] - 1, nx, ny))
            # 사이즈가 작거나 빈 공간인 경우
            elif shark_info[0] == field[nx][ny] or field[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
    choices.sort(key=lambda x: (x[0],x[1], x[2]))
    if not choices:
        break
    moves,x,y = choices[0]
    time += moves
    shark_info[1] += 1
    # 성장 조건 체크
    if shark_info[0] == shark_info[1]:
        shark_info[0] += 1
        shark_info[1] = 0
    field[shark_pos[0]][shark_pos[1]] = 0
    shark_pos = (x, y)
print(time)

# BFS로 이동 가능한 곳을 구하고 최단거리 물고기를 순차적으로 먹으면 되는 문제