def bellman_ford(st):
    dist = [int(1e9)] * N
    dist[st] = 0
    for i in range(N):
        for r in road:
            s, d, w = r[0], r[1], r[2]
            if dist[d] > dist[s] + w:
                dist[d] = dist[s] + w
                if i == N - 1:
                    return True
    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    road = []
    for _ in range(M):
        s, e, t = map(int, input().split())
        road.append((s-1, e-1, t))
        road.append((e-1, s-1, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        road.append((s-1, e-1, -t))

    to_past = bellman_ford(0)

    if to_past:
        print("YES")
    else:
        print("NO")
        
# 벨만포드
# float('inf') 쓰면 틀림