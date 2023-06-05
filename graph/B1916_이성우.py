import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [float('inf')]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0
    
    while q:
        d, now = heapq.heappop(q)
        
        if visited[now] < d:
            continue
        
        for i in graph[now]:
            cost = d + i[1]
            if cost < visited[i[0]]:
                visited[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(visited[end])