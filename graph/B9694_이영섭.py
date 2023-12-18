import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] >= dist:
            for pos, c in friend[now]:
                cost = dist + c

                if cost < distance[pos]:
                    path[pos] = now
                    q.append((cost, pos))
                    distance[pos] = cost


T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    friend = [[] for _ in range(M)]
    distance = [float("inf") for _ in range(M)]
    path = [-1 for _ in range(M)]

    for _ in range(N):
        x, y, z = map(int, input().split())
        friend[x].append((y, z))
        friend[y].append((x, z))

    dijkstra(0)

    ans = [M - 1]
    idx = M - 1
    while path[idx] != -1:
        idx = path[idx]
        ans.append(idx)

    ans = ans[::-1]
    if len(ans) == 1:
        ans = [-1]

    print(f"Case #{i + 1}: ", end='')
    print(*ans)
