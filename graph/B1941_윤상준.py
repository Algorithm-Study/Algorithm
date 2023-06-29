from collections import deque
field = [list(input()) for _ in range(5)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = []
def dfs(idx, s_count, y_count):
    x, y = idx // 5, idx % 5
    # 조건을 만족한 경우
    if s_count + y_count == 7 and s_count >= 4:
        visited = [[0] * 5 for _ in range(5)]
        count = 1
        queue = deque()
        queue.append(record[0])
        visited[record[0][0]][record[0][1]] = 1
        while queue:
            tx, ty = queue.popleft()
            for i in range(4):
                nx = tx + dx[i]
                ny = ty + dy[i]
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or visited[nx][ny]:
                    continue
                if (nx, ny) in record:
                    visited[nx][ny] = 1
                    count += 1
                    queue.append((nx, ny))
        if count == 7:
            result.append(1)
        return
    if y_count >= 4 or idx >= 25:
        return
    elif s_count + y_count == 7:
        return
    record.append((x, y))
    if field[x][y] == 'Y':
        dfs(idx + 1, s_count, y_count + 1)
    else:
        dfs(idx + 1, s_count + 1, y_count)
    record.pop()
    dfs(idx+1, s_count, y_count)


record = []
dfs(0, 0, 0)
print(sum(result))
# dp 방식을 활용하여 빠르게 최대 이동 횟수를 구해야 함