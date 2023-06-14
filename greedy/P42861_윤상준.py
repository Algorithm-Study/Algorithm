def solution(n, costs):
    costs.sort(key = lambda x: (x[2], x[0]))
    parent = [x for x in range(n)]
    cost = 0
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    def union(x1,x2):
        x1 = find(x1)
        x2 = find(x2)
        if x1 < x2:
            parent[x2] = x1
        else:
            parent[x1] = x2
    for c in costs:
        if find(c[0]) != find(c[1]):
            cost += c[2]
            union(c[0],c[1])
    return cost