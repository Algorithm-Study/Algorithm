import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(arr, start):
    global m
    distance = [INF]*(m+1)
    distance[start] = 0
    q = [(0, start)]
    path = [-1]*m

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for dist, next_ in arr[now]:
            new_cost = cost + dist

            if new_cost < distance[next_]:
                distance[next_] = new_cost
                path[next_] = now
                heapq.heappush(q, (new_cost, next_))
    return distance, path


t = int(input().rstrip())
for case in range(t):
    n, m = map(int, input().split())
    arr = [[] for _ in range(m)]
    for _ in range(n):
        x, y, z = map(int, input().split())
        arr[x].append((z, y))
        arr[y].append((z, x))

    distance, route = dijkstra(arr, 0)
    cost = distance[m-1]
    if cost == INF:
        print(f'Case #{case+1}: -1')
    else:
        answer = []
        node = m-1
        while node != -1:
            answer.append(node)
            node = route[node]
        print(f'Case #{case+1}:', *answer[::-1])