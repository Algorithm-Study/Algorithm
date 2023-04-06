import heapq
import sys
input = sys.stdin.readline
INF = int(1e10)

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

distance = [INF]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
start, end = map(int, input().split())

order = [0]*(n+1)
order[start] = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                order[i[0]] = now

dijkstra(start)

print(distance[end])
res = [end]

while order[end]:
    res.append(order[end])
    end = order[end]
print(len(res))
# print(order, res)
for _ in res[::-1]:
    print(_, end=' ')

# 이코테 다익스트라 문제2