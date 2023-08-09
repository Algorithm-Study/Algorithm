n, m = map(int, input().split())
arr = [[] for _ in range(n)]
visited = [False]*2001
answer = 0

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    

def dfs(num, cnt):
    global answer
    visited[num] = True
    
    if cnt == 4:
        answer = 1
        return
    
    for i in arr[num]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt+1)
            visited[i] = False
            
    visited[num] = False
            
for i in range(n):
    dfs(i, 0)
    if answer:
        break
    
print(answer)