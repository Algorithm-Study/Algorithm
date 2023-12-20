# 초기값 설정
n = int(input())
arr = list(map(int, input().split()))
dp = [[_ for _ in arr] for _ in range(2)]

# 제거 안했을 때와 제거 했을 때 dp 수행
for i in range(1, n):
    dp[0][i] = max(dp[0][i-1]+arr[i], dp[0][i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+arr[i])
print(max([max(_) for _ in dp]))