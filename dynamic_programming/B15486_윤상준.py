n = int(input())
consulting = []
dp = [0]*(n+1)
for _ in range(n):
    consulting.append(tuple(map(int, input().split())))
for i in range(1,n+1):
    time, profit = consulting[i-1]
    dp[i] = max(dp[i],dp[i-1])
    if i + time -1 <= n:
        dp[i + time -1] = max(dp[i-1] + profit, dp[i + time - 1])
print(max(dp))