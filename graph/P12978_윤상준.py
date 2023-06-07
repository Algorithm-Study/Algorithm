import sys
import heapq
INF = sys.maxsize
def solution(N, road, K):
    nodes = [[] for _ in range(N+1)]
    for r in road:
        x1, x2, time = r
        nodes[x1].append((x2, time))
        nodes[x2].append((x1, time))
    distance = [INF] * (N+1)
    queue = []
    heapq.heappush(queue,(0,1))
    distance[1] = 0
    while queue:
        cost, x = heapq.heappop(queue)
        if distance[x] < cost:
            continue
        for node in nodes[x]:
            cost2 = cost + node[1]
            if cost2 < distance[node[0]]:
                distance[node[0]] = cost2
                heapq.heappush(queue,(cost2, node[0]))
    answer = 0
    for dist in distance:
        if dist <= K:
            answer += 1
    return answer