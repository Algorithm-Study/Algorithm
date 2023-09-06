dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]
def dfs(node,record):
    x, y = node
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 사이클 구성이 가능한 경우
        if (nx,ny) == record[0] and (nx,ny) != record[-2]:
            print('Yes')
            exit()
        # 이전과 같은 값을 가지고 방문한 적이 없는 경우
        if not visited[nx][ny] and field[nx][ny] == field[x][y]:
            visited[nx][ny] = 1
            dfs((nx,ny), record + [(nx,ny)])
record = []
for i in range(n):
    for j in range(m):
        visited = [[0]*m for _ in range(n)]
        visited[i][j] = 1
        dfs((i,j), record + [(i,j)])
print('No')
#압력이 작아서 전체에 대해서 탐색해도됨