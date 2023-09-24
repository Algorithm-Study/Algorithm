import heapq, sys
INF = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
queue = []
distance[1] = 0
shortest_path = [0]*(n+1)
heapq.heappush(queue,(0,1))
while queue:
    dist, current = heapq.heappop(queue)
    if distance[current] < dist:
        continue
    for g, cost in graph[current]:
        new_dist = dist + cost
        if new_dist < distance[g]:
            distance[g] = new_dist
            shortest_path[g] = current
            heapq.heappush(queue, (new_dist, g))
# 무조건 n-1개 존재
print(n-1)
for i in range(2,n+1):
    print(i,shortest_path[i])
# 간선 연결이 갱신될 값을 저장했다가 출력하면 되는 문제