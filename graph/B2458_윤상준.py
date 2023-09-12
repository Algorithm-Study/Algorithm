n, m = map(int, input().split())
dist = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    dist[a][b] = 1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if dist[i][k] + dist[k][j] == 2:
                dist[i][j] = 1
total = 0
for i in range(1,n+1):
    temp = 0
    for j in range(1,n+1):
        temp += dist[i][j] + dist[j][i]
    if temp == n-1:
        total += 1
print(total)
# 자신과 연결된 경우의 수가 n-1 인지 체크하면 되는 문제