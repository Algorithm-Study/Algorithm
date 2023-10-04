import heapq
n, m = map(int, input().split())
degree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1
queue = []
for i in range(1,n+1):
    if not degree[i]:
        heapq.heappush(queue, i)
result = []
while queue:
    to_solve = heapq.heappop(queue)
    result.append(to_solve)
    for g in graph[to_solve]:
        degree[g] -= 1
        if not degree[g]:
            heapq.heappush(queue, g)
print(*result)
# 의존성에 따라서 단계를 높이는 방식으로 진행하면 됨