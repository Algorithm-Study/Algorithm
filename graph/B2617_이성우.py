import sys
input = sys.stdin.readline

N, M = map(int, input().split())

heavy = [[] for _ in range(N+1)]
light = [[] for _ in range(N+1)]
mid = (N+1)/2

for _ in range(M):
    a, b = map(int, input().split())
    heavy[b].append(a)
    light[a].append(b)

def dfs(arr, n):
    global cnt
    for i in arr[n]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(arr,i)

answer = 0
for i in range(1, N+1):
    visited = [False]*(N+1)
    cnt = 0
    dfs(heavy, i)
    if cnt >= mid:
        answer += 1
    cnt = 0
    dfs(light, i)
    if cnt >= mid:
        answer += 1

print(answer)