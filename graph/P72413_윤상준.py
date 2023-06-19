import heapq,sys
INF = sys.maxsize
def solution(n, s, a, b, fares):
    answer = INF
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        x,y,fee = fare
        graph[x].append((y,fee))
        graph[y].append((x,fee))
    def dijkstra(n,s,e):
        fees = [INF] * (n+1)
        queue = []
        heapq.heappush(queue, (0, s))
        fees[s] = 0
        while queue:
            fee, start = heapq.heappop(queue)
            if fees[start] < fee:
                continue
            for g in graph[start]:
                cost = fee + g[1]
                if cost < fees[g[0]]:
                    fees[g[0]] = cost
                    heapq.heappush(queue,(cost, g[0]))
        return fees[e]
    for i in range(1,n+1):
        a_route = dijkstra(n,i,a)
        b_route = dijkstra(n,i,b)
        if i != s:
            together = dijkstra(n,s,i)
        else:
            together = 0
        answer = min(answer, a_route + b_route + together)
    return answer
# 각 인원별 최소 경로를 구한 후 공통 구간을 계산하는 방식으로는 해결 불가능
# 같이 타는 구간, 개별 구간으로 나눠서 계산해야 문제 해결 가능