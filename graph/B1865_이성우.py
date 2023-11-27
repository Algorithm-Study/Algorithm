import sys
input = sys.stdin.readline
INF = 1e9

# 벨만 포드
def bellman_ford(start):
    dist[start] = 0
    
    # n번 라운드 반복
    for i in range(1, n+1):
        # 매 라운드 모든 간선 확인
        for j in range(len(edges)):
            now, next_, cost = edges[j]
            # 현재 간선을 통해 다른 노드로 이동하는 거리가 더 짧을 때
            # dist[now] != INF 일 때 방문하지 않으면 초기 음의 사이클 노드들과 연결되지 않게 돼 버그 발생
            if dist[next_] > dist[now] + cost:
                dist[next_] = dist[now] + cost
                # n번째 라운드에서 값이 갱신되면 음의 사이클 발생
                if i == n:
                    return True
    return False

# 변수 초기화
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    dist = [INF]*(n+1)
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
        
    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))
    
    if bellman_ford(1):
        print('YES')
    else:
        print('NO')
