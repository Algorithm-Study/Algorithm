import heapq
import sys
INF = sys.maxsize
T = int(input())
# 테스트 케이스
def dijkstra(start):
    queue = [[0,start]]
    dist = [INF]*(n+1)
    dist[start] = 0
    while queue:
        cost, node = heapq.heappop(queue)
        if dist[node] < cost:
            continue
        for distance, next_node in graph[node]:
            if dist[next_node] > distance + cost:
                dist[next_node] = distance + cost
                heapq.heappush(queue,(distance + cost, next_node))
    return dist
for _ in range(T):
    #n : 교차점, m: 도로, t: 목적지 후보의 개수
    n, m, t = map(int, input().split())
    #s : 시작점, g,h : 반드시 지나는 경로
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
    destination = []
    for _ in range(t):
        destination.append(int(input()))
    dist_s = dijkstra(s)
    # 먼 곳에 대해서 다익스트라 한 번 더 진행
    if dist_s[g] < dist_s[h]:
        via = h
    else:
        via = g
    dist_v = dijkstra(via)
    result  = []
    for dest in destination:
        if dist_s[via] + dist_v[dest] == dist_s[dest]:
            result.append(dest)
    print(*sorted(result))
# 2단계 다익스트라를 진행하는 문제