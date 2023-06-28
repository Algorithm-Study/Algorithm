import sys
sys.setrecursionlimit(10**5)
n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited  = [[0]*n for _ in range(n)]
def dfs(x,y):
    if visited[x][y] != 0:
        return visited[x][y]
    visited[x][y] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >=n or ny>=n:
            continue
        if field[nx][ny] > field[x][y]:
            visited[x][y] = max(visited[x][y], dfs(nx,ny)+1)
    return visited[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i,j))
print(answer)
# 대나무 숲의 크기가 최대 500이어서 매 위치마다 이동 횟수를 구하면 시간 초과
# 각 위치별 방문 자리를 저장하여 다른 곳에서 해당 위치로 방문한 경우 방문 횟수를 제공해야 시간 안에 해결 가능