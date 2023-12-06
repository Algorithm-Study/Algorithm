import heapq

N = int(input())
A, B, C = map(int, input().split())
M = int(input())
road = [[] for _ in range(N+1)]

for _ in range(M):
    D, E, L = map(int, input().split())
    road[D].append((E, L))
    road[E].append((D, L))


def dijkstra(start):
    dist = [float('inf')] * (N+1)
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        dis, cx = heapq.heappop(pq)
        if dist[cx] < dis:
            continue
        for nx in road[cx]:
            cost = dis + nx[1]
            if cost < dist[nx[0]]:
                dist[nx[0]] = cost
                heapq.heappush(pq, (cost, nx[0]))
    return dist


AD, BD, CD = dijkstra(A), dijkstra(B), dijkstra(C)
ans = 0
for i in range(1, N+1):
    min_val = min(AD[i], BD[i], CD[i])
    if min_val > ans:
        ans = min_val
        answer = i
print(answer)
