import sys
from collections import deque
def solution(n, edge):
    answer = 0
    INF = sys.maxsize
    distance = [INF]*(n+1)
    visited = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for e in edge:
        x,y = e
        graph[x].append(y)
        graph[y].append(x)
    queue = deque()
    queue.append([1,0])
    distance[1], visited[1] = 0, 1
    while queue:
        x,cost = queue.popleft()
        for g in graph[x]:
            if visited[g] == 0:
                visited[g] = 1
                queue.append([g,cost+1])
                distance[g] = cost + 1
    max_distance = max(distance[1:])
    
    return sum([1 for d in distance if d == max_distance])
# 그래프 거리 구해서 최대값만 구해서 합하면 끝 -> 기본 유형 문제라서 시간 초과도 고려할 필요X