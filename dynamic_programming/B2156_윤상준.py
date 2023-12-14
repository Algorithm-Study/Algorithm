n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [0] * n
if n <= 2:
    print(sum(wines))
    exit()
dp[0] = wines[0]
dp[1] = wines[0] + wines[1]
for i in range(2, n):
    dp[i] = max(dp[i-3] + wines[i-1] + wines[i], dp[i-2] + wines[i], dp[i-1])

print(max(dp))