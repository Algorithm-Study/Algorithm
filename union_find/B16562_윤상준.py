n,m,k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
parent = [x for x in range(n+1)]
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    pa, pb = find(a), find(b)
    if cost[pa] < cost[pb]:
        parent[pb] = parent[pa]
    else:
        parent[pa] = parent[pb]
for _ in range(m):
    a, b = map(int, input().split())
    union(a,b)
result = set()
for i in range(1,n+1):
    result.add(find(i))
price = sum(cost[x] for x in result)
if price <= k:
    print(price)
else:
    print('Oh no')