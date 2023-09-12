from collections import deque

n, m = map(int, input().split())

tall = [[]*n for _ in range(n)]
short = [[]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    tall[a-1].append(b-1)
    short[b-1].append(a-1)
    
def bfs(x, arr):
    q = deque()
    q.append(x)
    visited = [False]*n
    visited[x] = True
    cnt = 0
    
    while q:
        i = q.popleft()
        
        for j in arr[i]:
            if visited[j] == False:
                q.append(j)
                visited[j] = True
                cnt += 1
    return cnt
answer = 0
for i in range(n):
    cnt = bfs(i, tall) + bfs(i, short)
    if cnt == n-1:
        answer += 1
        
print(answer)

# 플로이드 워셜로도 풀 수 있음