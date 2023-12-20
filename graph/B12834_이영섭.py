import heapq


def dijkstra(start, comp):
    distance[start][comp] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        dist, node = heapq.heappop(pq)
        if distance[node][comp] < dist:
            continue
        for nxt in graph[node]:
            cost = nxt[1] + dist
            if distance[nxt[0]][comp] > cost:
                distance[nxt[0]][comp] = cost
                heapq.heappush(pq, (cost, nxt[0]))


N, V, E = map(int, input().split())
A, B = map(int, input().split())
home = list(map(int, input().split()))
graph = [[] for _ in range(V+1)]
distance = [[int(1e8), int(1e8)] for _ in range(V+1)]
for _ in range(E):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
dijkstra(A, 0)
dijkstra(B, 1)
ans = 0

for i in home:
    if distance[i][0] == float('inf'):
        distance[i][0] = -1
    if distance[i][1] == float('inf'):
        distance[i][1] = -1
    ans += distance[i][0] + distance[i][1]
print(ans)