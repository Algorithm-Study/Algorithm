n = int(input())
arr = list(map(int, input().split()))

# 초기값 설정
dp = [[0]*21 for _ in range(n)]
dp[0][arr[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j]:
            # 더할 때
            if 0 <= j+arr[i] <= 20:
                dp[i][j+arr[i]] += dp[i-1][j]
            # 뺄 때
            if 0 <= j-arr[i] >= 0:
                dp[i][j-arr[i]] += dp[i-1][j]
                
print(dp[n-2][arr[n-1]])