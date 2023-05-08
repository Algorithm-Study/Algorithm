N = int(input())
dp = [0 for _ in range(30)]
dp[1] = 3
for i in range(3, N, 2):
    dp[i] = dp[i-2] * 3 + 2
    for j in range(3, i, 2):
        dp[i] += dp[i-j-1] * 2
print(dp[N-1])

# 문제 접근 방법
# # dp[i-2] * 3 + 2로 시도하다가 계속 틀림
# # 특이 케이스가 반복될 수 있어서 더해줌