n, E, W, S, N = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

prob = [E, W, S, N]
answer = 0

def dfs(x, y, visited, cnt, p):
    global answer
    if cnt == n:
        answer += p
        return
    
    visited.add((x, y))
    
    for d in range(4):
        if prob[d] != 0:
            nx, ny = x + dx[d], y + dy[d]
            
            if not (nx, ny) in visited:
                visited.add((nx, ny))
                dfs(nx, ny, visited, cnt+1, p*(prob[d]/100))
                visited.remove((nx, ny))

                
dfs(0, 0, set(), 0, 1)
print(answer)