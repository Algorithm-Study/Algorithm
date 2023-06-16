import heapq
import sys
INF = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
q = [(0,1)]
distance[1] = 0
while q:
    c1, start = heapq.heappop(q)
    for g in graph[start]:
       end,c2 = g
       c3 = c1 + c2
       if distance[end] > c3:
           distance[end] = c3
           heapq.heappush(q, (c3, end))
print(distance[n])
# 다익스트라 기본 유형 문제