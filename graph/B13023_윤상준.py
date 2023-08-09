n, m = map(int, input().split())
graphs = [[] for _ in range(n)]
visited = [0]*n
def dfs(idx, depth):
    global possible
    visited[idx] = 1
    if depth == 4:
        print(1)
        exit()
    for g in graphs[idx]:
        if visited[g] == 0:
            visited[g] = 1
            dfs(g, depth + 1)
            visited[g] = 0
for _ in range(m):
    a,b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)
for i in range(n):
    dfs(i,0)
    visited[i] = False
print(0)

# 5명의 조합이 가능한지 확인해서 가능한 경우 출력하고 끝