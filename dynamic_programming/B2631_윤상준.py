n = int(input())
dp = [1]*(n+1)
line = [0] + [int(input()) for _ in range(n)]
for i in range(1,n+1):
    for j in range(1,i):
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))

# 전형적인 LIS 문제
# 전체 길이에서 LIS를 빼주면 문제해결 가능