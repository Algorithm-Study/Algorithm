N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
prefix_sum = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + board[i-1][j-1] - prefix_sum[i-1][j-1]

ans = float("-INF")
for x1 in range(1, N+1):
    for y1 in range(1, M+1):
        for x2 in range(x1, N+1):
            for y2 in range(y1, M+1):
                ans = max(ans, prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1])
print(ans)