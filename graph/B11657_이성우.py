import sys
input = sys.stdin.readline
INF = sys.maxsize

# 벨만 포드 구현
def bellman_ford(start):
    dist[start] = 0
    
    # n번 라운드 반복
    for i in range(1, n+1):
        # 매 라운드에 모든 간선 확인
        for j in range(m):
            now, next_, cost = edges[j]
            # 현재 간선을 통해 다른 노드로 이동하는 거리가 더 짧으면
            if dist[now] != INF and dist[next_] > dist[now] + cost:
                dist[next_] = dist[now] + cost
                # n번째 라운드에서 값이 갱신된다면 음수 순환이 존재
                if i == n:
                    return True
    return False

# 변수 초기화
n, m = map(int, input().split())
edges = []
dist = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    
negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        # 도달 불가능
        if dist[i] == INF:
            print(-1)
        # 도달 가능
        else:
            print(dist[i])