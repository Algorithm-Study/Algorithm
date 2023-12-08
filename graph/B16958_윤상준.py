import sys
input = sys.stdin.readline
INF = 10000
n, t = map(int, input().rstrip().split())
nodes = []
t_nodes = []
distance = []
for i in range(n):
    s, x, y = map(int, input().rstrip().split())
    nodes.append([x, y])
    if s:
        t_nodes.append([x, y])
for point in nodes:
    x1, y1 = point
    node_value = INF
    for teleportable_point in t_nodes:
        x2, y2 = teleportable_point
        manhattan = abs(x1-x2) + abs(y1-y2)
        if manhattan < node_value :
            node_value = manhattan
    distance.append(node_value) 

m = int(input())
for _ in range(m):
    start, end = map(int, input().rstrip().split())
    x1, y1 = nodes[start-1]
    x2, y2 = nodes[end-1]
    print(min(abs(x1-x2) + abs(y1-y2), distance[start-1] + t + distance[end-1]))

# 문제 이동 조건은 총 4가지
# 1. 두 정점 간에 순간이동이 가능한 경우: t
# 2. 시작점은 순간이동이 가능한 경우: 도착점과 인접한 점으로 순간이동 후 맨하탄 거리
# 3. 도착점은 순간이동이 가능한 경우: 시작점과 인접한 점으로 맨하탄 거리 이동 후 순간 이동
# 4. 두 정점 간에 순간이동이 불가능한 경우: 맨하탄 거리
# 순간이동이 없을 경우 중간 지점을 방문할 필요가 없는 문제
# 위 4가지 조건을 이해하면 플로이드 워셜로 진행할 필요가 없음