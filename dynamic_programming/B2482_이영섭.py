N = int(input())
K = int(input())
dp = [[0]*(N+1) for _ in range(N+1)]
# n개의 색, k개를 선택, 이번에 선택 o/x
for i in range(1, N+1):
    dp[i][1] = i
    dp[i][0] = 1

for i in range(3, N+1):
    for j in range(2, (i+1)//2 + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1]) % 1_000_000_003

print((dp[N - 3][K - 1] + dp[N - 1][K]) % 1_000_000_003)
