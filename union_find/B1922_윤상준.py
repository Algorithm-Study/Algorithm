n = int(input())
m = int(input())
parent = [x for x in range(n+1)]
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))
edges.sort()
def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(a,b):
    p1,p2 = find(a),find(b)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2
total = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a,b)
        total += cost
print(total)
        