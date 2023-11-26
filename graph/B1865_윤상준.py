INF = int(1e9)
t = int(input())
for _ in range(t):
    n,m,w = map(int, input().split())
    distance = [INF]*(n+1)
    distance[1] = 0
    edges = []
    for i in range(m):
        s,e,c = map(int, input().split())
        edges.append((s,e,c))
        edges.append((e,s,c))
    for j in range(w):
        s,e,c = map(int, input().split())
        edges.append((s,e,-c))
    cycle = 0
    for i in range(n):
        for edge in edges:
            a, b, cost = edge
            # 최소 거리 조건이 아니라 사이클 여부만 판단하면 되기 떄문에 distance[a] != INF 조건이 필요 없음
            if distance[b] > distance[a] + cost:
                distance[b] = distance[a] + cost
                if i == n-1:
                    cycle = 1
    print('YES' if cycle == 1 else 'NO')