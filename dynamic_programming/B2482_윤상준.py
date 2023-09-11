n = int(input())
k = int(input())
div = 1_000_000_003
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0], dp[i][1] = 1,i
# i개가 있을 때 k개를 선택하는 경우의 수
for i in range(2,n+1):
    for j in range(2,k+1):
        # N번째 수를 선택하는 경우 + N번째 수를 선택하지 않는 경우 = i개 중에서 K개를 선택하는 경우
        dp[i][j] = (dp[i-2][j-1] + dp[i-1][j])%div
print((dp[n-3][k-1] + dp[n-1][k])%div)
# 처음부터 원으로 생각하지 말고 직선으로 점화식 세운 다음에 원인 경우 생각하기