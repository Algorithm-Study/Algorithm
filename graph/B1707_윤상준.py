t = int(input())
def dfs(start, g) -> bool:
    visited[start] = g
    for node in graphs[start]:
        if visited[node] == 0:
            avail = dfs(node, -g)
            if not avail:
                return False
        elif visited[node] == visited[start]:
            return False
    return True

for _ in range(t):
    v, e = map(int, input().split())
    graphs = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    for _ in range(e):
        a, b = map(int, input().split())
        graphs[a].append(b)
        graphs[b].append(a)
    for i in range(1,v+1):
        if visited[i] == 0:
            avail = dfs(i,1)
            if not avail:
                break
    if avail:
        print('YES')
    else:
        print('NO')