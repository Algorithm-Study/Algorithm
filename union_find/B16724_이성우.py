import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, cnt):
    global answer
    if visited[x][y] != 0:
        if visited[x][y] == cnt:
            answer += 1
        return
    
    visited[x][y] = cnt
    i = direction.index(arr[x][y])
    dfs(x+dx[i], y+dy[i], cnt)
    
cnt = 1
answer = 0
for i in range(n):
    for j in range(m):
        dfs(i, j, cnt)
        cnt += 1
        
print(answer)

