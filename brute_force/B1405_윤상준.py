n, east, west, south, north = map(int, input().split())
probs = [north*0.01, west*0.01, south*0.01, east*0.01]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cases = []
def dfs(x,y, visited, probability):
    if len(visited) == n+1:
        cases.append(probability)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) not in visited:
                visited.append((nx,ny))
                dfs(nx,ny,visited,probability*probs[i])
                visited.pop()
dfs(0,0,[(0,0)], 1)
print(sum(cases))
# 한번보다 많이 이동하지 않는 조건으로 인해 방문하지 않도록 하는 처리 필요
