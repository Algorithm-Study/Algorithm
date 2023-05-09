# 초기 변수값
n = int(input())
dp = [0]*31

dp[0] = 1
dp[2] = 3

# 점화식 계산
for idx in range(4,n+1,2):
    dp[idx] = dp[idx-2]*3 + sum(dp[:idx-2])*2

print(dp[n])