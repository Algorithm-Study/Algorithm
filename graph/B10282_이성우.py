import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

tc = int(input())

def dijkstra(num):
    distance = [INF]*(n+1)
    
    q = []
    distance[num] = 0
    heapq.heappush(q, (0, num))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in arr[now]:
            cost = dist + i[0]
            
            if distance[i[1]] > cost:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

    return distance

for _ in range(tc):
    n, d, c = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        arr[b].append((s, a))

    answer = dijkstra(c)
    cnt = 0
    tme = 0
    for a in answer:
        if a != INF:
            cnt += 1
            tme = max(tme, a)
            
    print(cnt, tme)