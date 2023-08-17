n, m = map(int, input().split())
dist = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    heavy, light = map(int, input().split())
    dist[heavy][light] = 1
#플로이드 워셜
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if dist[j][i] + dist[i][k] == 2:
                dist[j][k] = 1
case = 0
for i in range(1,n+1):
    light_ball = 0
    heavy_ball = 0
    for j in range(1,n+1):
        if i == j:
            continue
        elif dist[i][j]:
            light_ball += 1
        elif dist[j][i]:
            heavy_ball += 1
    if light_ball > n//2 or heavy_ball > n//2:
        case += 1
print(case)
# 플로이드 워셜 방법으로 해결