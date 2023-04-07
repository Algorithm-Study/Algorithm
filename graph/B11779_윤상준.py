import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
route = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append((y,cost))
start, end = map(int ,input().split())
INF = 1e9
cost = [INF] * (n+1)
queue = []
heapq.heappush(queue, (start, 0))
cost[start] = 0
route[start].append(start)
while queue:
    x, val = heapq.heappop(queue)
    if cost[x] < val:
        continue
    for i in graph[x]:
            value = val + i[1]
            if value < cost[i[0]]:
                cost[i[0]] = value
                temp = route[x] +[i[0]]
                route[i[0]] = temp[:]
                heapq.heappush(queue,(i[0], value))
print(cost[end])
print(len(route[end]))
for r in route[end]:
    print(r, end=' ')