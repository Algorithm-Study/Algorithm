N, M = map(int, input().split())
road = [[int(1e9)]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    road[a][b] = t

K = int(input())
city = list(map(int, input().split()))

for i in range(N+1):
    for j in range(N+1):
        road[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if road[i][k] + road[k][j] < road[i][j]:
                road[i][j] = road[i][k] + road[k][j]

min_val = float('inf')
ans = []
for i in range(1, N+1):
    max_val = 0
    for c in city:
        max_val = max(max_val, road[c][i] + road[i][c])
    if min_val > max_val:
        min_val = max_val
        ans = [i]
    elif min_val == max_val:
        ans.append(i)
print(*ans)
