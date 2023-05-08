import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(cx, cy):
    if cx == M-1 and cy == N-1:
        return 1
    if visit[cx][cy] != -1:
        return visit[cx][cy]

    temp = 0
    for dir in range(4):
        nx, ny = cx + dx[dir], cy + dy[dir]
        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue
        if board[nx][ny] >= board[cx][cy]:
            continue
        temp += dfs(nx, ny)
    visit[cx][cy] = temp
    return visit[cx][cy]


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
visit = [[-1]*N for _ in range(M)]
print(dfs(0, 0))

# 문제 접근 방법
# # 일반적인 dfs로 접근하면 제한 시간 내에 문제를 풀 수 없다.
# # 메모이제이션을 사용한 방법으로 이전에 방문했던 좌표이면 그 값을 저장한다.