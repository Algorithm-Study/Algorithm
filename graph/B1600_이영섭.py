from collections import deque

K = int(input())
W, H = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [-1, 1, -2, 2, -2, 2, -1, 1]

board = [list(map(int, input().split())) for _ in range(H)]
visit = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]


def bfs(horse_move):
    dq = deque()
    dq.append((0, 0, 0))
    visit[0][0][0] = 1
    while dq:
        cx, cy, K = dq.popleft()
        if K < horse_move:
            for dir in range(8):
                nx, ny = cx + hx[dir], cy + hy[dir]
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                if board[nx][ny] == 1 or visit[nx][ny][K+1] > 0:
                    continue
                dq.append((nx, ny, K+1))
                visit[nx][ny][K+1] = visit[cx][cy][K] + 1
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if board[nx][ny] == 1 or visit[nx][ny][K] > 0:
                continue
            dq.append((nx, ny, K))
            visit[nx][ny][K] = visit[cx][cy][K] + 1
    ans = 10e8
    for i in range(horse_move+1):
        if visit[H-1][W-1][i]:
            ans = min(ans, visit[H-1][W-1][i])
    if ans != 10e8:
        return ans - 1
    else:
        return -1


print(bfs(K))

# 문제 접근 방법
# # 말처럼 이동할 수 있는 visit을 K개 따로 만들어주고 마지막 칸의 min값을 구함