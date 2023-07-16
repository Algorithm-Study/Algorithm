n,m = map(int, input().split())
field = [list(input()) for _ in range(n)]
result = 0
ways = [(-1,1),(0,1),(1,1)]
def dfs(x,y):
    if y == m-1:
        return 1
    for way in ways:
        nx, ny = x + way[0], y+ way[1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if field[nx][ny] == '.':
            field[nx][ny] = 'w'
            if dfs(nx,ny):
                return 1
    return 0

for i in range(n):
    result += dfs(i,0)
print(result)
# 그리디하게 탐색하면 됨
# 모든 조건을 찾으려고 할 필요가 없는 문제