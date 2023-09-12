from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
field = [list(map(int, input().split())) for _ in range(3)]
start = ''.join([''.join([str(i) for i in x]) for x in field])
visited = {}
queue = deque()
queue.append(start)
visited[start] = 0
while queue:
    current = queue.popleft()
    zero = current.index('0')
    x,y = zero//3, zero%3
    if current == '123456780':
        print(visited[current])
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= 3 or ny >= 3:
            continue
        new_zero = nx*3 + ny
        new_current = list(current)
        new_current[zero], new_current[new_zero] = new_current[new_zero], new_current[zero]
        new_current = ''.join(new_current)
        if new_current not in visited:
            visited[new_current] = visited[current] + 1
            queue.append(new_current)
print(-1)
# 방문을 딕셔너리로 처리해야 함