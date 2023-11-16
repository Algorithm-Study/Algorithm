from itertools import combinations

N, M = map(int, input().split())
city = [[float('inf')]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    city[a][b] = 1
    city[b][a] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            city[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if city[a][b] > city[a][k] + city[k][b]:
                city[a][b] = city[a][k] + city[k][b]

bf = combinations([i for i in range(1, N+1)], r=2)
min_val = float('inf')
ans = []
for case in bf:
    val = 0
    for k in range(1, N+1):
        val += min(city[k][case[0]], city[k][case[1]]) * 2
    if val < min_val:
        min_val = val
        ans = [case[0], case[1], val]
print(*ans)
