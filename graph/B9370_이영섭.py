import heapq
from collections import defaultdict

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    road = defaultdict(list)
    distances = [int(1e9) for _ in range(n+1)]
    check = [0]*(n+1)
    ep = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        road[a].append((b, d))
        road[b].append((a, d))
    for _ in range(t):
        ep.append(int(input()))
    ep.sort()
    hp = []
    heapq.heappush(hp, (0, s))
    distances[s] = 0
    # print(road)
    while hp:
        dis, idx = heapq.heappop(hp)
        # print("거리",dis, "번호",idx, "방문여부",visited)
        if distances[idx] < dis:
            continue
        for nxt, ndis in road[idx]:
            new_dist = dis + ndis
            # print("추가할거리",ndis, "방문할 번호",nxt, "새거리",new_dist)
            if distances[nxt] > new_dist:
                distances[nxt] = new_dist
                heapq.heappush(hp, [new_dist, nxt])
                check[nxt] = check[idx]
                if (idx == g and nxt == h) or (idx == h and nxt == g):
                    check[nxt] = 1
            elif distances[nxt] == new_dist:
                check[nxt] = max(check[nxt], check[idx])
                if (idx == g and nxt == h) or (idx == h and nxt == g):
                    check[nxt] = 1
    # print(distances)
    for e in ep:
        # print(e, distances[e])
        if check[e]:
            print(e, end=" ")
    print()
