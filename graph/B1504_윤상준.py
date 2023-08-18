import sys
import heapq
n,e = map(int, input().split())
graphs = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,cost = map(int, input().split())
    graphs[a].append((b,cost))
    graphs[b].append((a,cost))
v1, v2 = map(int, input().split())
check = [1,v1,v2]
p1,p2 = 0,0
for i in range(3):
    distance = [sys.maxsize for _ in range(n+1)]
    queue = []
    heapq.heappush(queue,(0,check[i]))
    distance[check[i]] = 0
    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue
        for g in graphs[now]:
            cost = dist + g[1]
            if distance[g[0]] > cost:
                distance[g[0]] = cost
                heapq.heappush(queue,(cost,g[0]))
    if i == 0:
        p1 += distance[v1]
        p2 += distance[v2]
    elif i == 1:
        p1 += distance[v2]
        p2 += distance[n]
    else:
        p1 += distance[n]
        p2 += distance[v1]
result = min(p1,p2)
if result >= sys.maxsize:
    print(-1)
else:
    print(result)