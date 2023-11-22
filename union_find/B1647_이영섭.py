def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

parent = [i for i in range(n + 1)]
graph.sort()
line = []
ans = 0

for c, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        ans += c
        line.append(c)
ans -= line.pop()

print(ans)
