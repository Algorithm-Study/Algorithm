import sys
imput = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def dfs(x, y):
    if y == m-1:
        return True
    
    for dx in [-1, 0, 1]:
        nx = x + dx
        ny = y + 1
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] != 'x' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
    return False


answer = 0
for i in range(n):
    if dfs(i, 0):
        answer += 1
        
print(answer)
