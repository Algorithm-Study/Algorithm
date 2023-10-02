from collections import defaultdict
import heapq

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    computer = defaultdict(list)
    distance = [float('inf') for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        computer[b].append((s, a))

    pq = [(0, c)]
    distance[c] = 0
    while pq:
        tm, cx = heapq.heappop(pq)
        if distance[cx] < tm:
            continue
        for nxt_tm, nx in computer[cx]:
            new_tm = nxt_tm + tm
            if distance[nx] <= new_tm:
                continue
            distance[nx] = new_tm
            heapq.heappush(pq, (new_tm, nx))
            ans = new_tm

    cnt, ans = 0, 0
    for dist in distance:
        if dist != float('inf'):
            cnt += 1
            ans = max(ans, dist)

    print(cnt, ans)
