import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
fee = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, f = map(int, input().split())
    fee[s].append((e, f))
st, ed = map(int, input().split())


def dijkstra(graph, start):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])

    while queue:
        dist, node = heapq.heappop(queue)

        # 기존 최단거리보다 멀다면 무시
        if distance[node] < dist:
            continue

        # 노드와 연결된 인접노드 탐색
        for next_node, next_dist in graph[node]:
            dista = dist + next_dist # 인접노드까지의 거리
            if dista < distance[next_node]: # 기존 거리보다 짧으면 갱신
                distance[next_node] = dista
                heapq.heappush(queue, [dista, next_node]) # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    return distance


dist_start = dijkstra(fee, st)
print(dist_start[ed])

# 문제 접근 방법
# # 다익스트라 알고리즘을 사용하여 해결할 수 있음
# # 출발지에서 가까운 지점부터 차례대로 최단경로를 탐색하며, 목적지까지의 최단경로를 탐색하는 알고리즘
# # 그리디 알고리즘 기법으로, 한 번 결정된 최단 경로는 절대 바뀌지 않으며 이를 바탕으로 목적지까지의 최단경로를 계산
# # 최단 거리뿐만 아니라 경로 추적에도 사용할 수 있음