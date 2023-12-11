N = int(input())
work, dp = [], [0]*(N+1)
for _ in range(N):
    t, p = map(int, input().split())
    work.append((t, p))
for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    day = i + work[i-1][0] - 1
    if day <= N:
        dp[day] = max(dp[day], dp[i-1] + work[i-1][1])
print(max(dp))
