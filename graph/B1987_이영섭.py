R, C = map(int, input().split())
board = [input() for _ in range(R)]
visit = [[0]*C for _ in range(R)]
ans = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dq = set()
dq.add((0, 0, board[0][0]))
visit[0][0] = 1

while dq:
    cx, cy, alp = dq.pop()
    for dir in range(4):
        nx = cx + dx[dir]
        ny = cy + dy[dir]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if board[nx][ny] in alp:
            continue
        dq.add((nx, ny, alp+board[nx][ny]))
        ans = max(ans, len(alp)+1)

print(ans)

# 문제 접근 방법
# # deque으로 하니까 메모리초과
# # set으로 바꿔놓고 지나온 것 하나씩 탐색하니까 시간초과
# # visit을 ans로 바꾸면서 ans 값을 0으로 초기화해서 틀렸습니다. 