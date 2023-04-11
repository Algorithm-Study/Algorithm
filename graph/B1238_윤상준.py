import heapq
import sys
input = sys.stdin.readline
n, m, goal = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
    i, j, cost = map(int, input().split())
    graph[i].append((j, cost))

def field(start):
    queue = []
    distance = [INF]*(n+1)
    heapq.heappush(queue, (start, 0))
    distance[start] = 0
    while queue:
        current, charge = heapq.heappop(queue)
        if distance[current] < charge:
            continue
        for end, time in graph[current]:
            total_time = charge + time
            if total_time < distance[end]:
                distance[end] = total_time
                heapq.heappush(queue, (end, total_time))
    return distance
student = field(goal)
for i in range(1,n+1):
    if i != goal:
        to = field(i)
        student[i] += to[goal]
print(max(student[1:]))