def union(a, b):
    a, b = find(a), find(b)
    if cost[a] < cost[b]:
        parent[b] = a
    else:
        parent[a] = b


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


N, M, k = map(int, input().split())
parent = list(i for i in range(N+1))
cost = [0] + list(map(int, input().split()))
for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)
ans = 0
friend = set()
for i in range(1, N+1):
    if find(i) not in friend:
        ans += cost[parent[i]]
        friend.add(parent[i])

if ans > k:
    print("Oh no")
else:
    print(ans)
