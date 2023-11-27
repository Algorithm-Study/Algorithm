N, M = map(int, input().split())
bus = []
for _ in range(M):
    a, b, c, = map(int, input().split())
    bus.append((a-1, b-1, c))
dist = [float('inf') for _ in range(N)]


def bellman_ford(st):
    dist[0] = 0
    for i in range(N):
        for j in range(M):
            s, d, w = bus[j][0], bus[j][1], bus[j][2]
            if dist[s] != float('inf') and dist[d] > dist[s] + w:
                dist[d] = dist[s] + w
                if i == N - 1:
                    return True
    return False


to_past = bellman_ford(0)
if to_past:
    print(-1)
else:
    for i in range(1, N):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])

# 벨만포드