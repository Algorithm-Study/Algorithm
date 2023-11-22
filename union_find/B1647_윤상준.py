n, m = map(int, input().split())
routes = []
parent = [x for x in range(n+1)]
for _ in range(m):
    routes.append(list(map(int, input().split())))
routes.sort(key = lambda x : x[2])
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    pa, pb = find(a), find(b)
    if pa < pb:
        parent[pb] = parent[pa]
    else:
        parent[pa] = parent[pb]
result = 0
for a,b, cost in routes:
    if find(a) != find(b):
        union(a,b)
        result += cost
        temp = cost
print(result-temp)