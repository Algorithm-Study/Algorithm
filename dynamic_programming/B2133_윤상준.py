# 규칙성 찾기 2의 배수 길이 만큼 특수한 조합이 2개씩 나타남
n = int(input())
if n % 2 != 0:
    print(0)
    exit()
dp = [0]*31
dp[0] = 1
dp[2] = 3

for i in range(4,n+1):
    dp[i] = dp[i-2] * dp[2]
    for j in range(i-4, -1, -2):
        dp[i] += dp[j]*2
print(dp[n])
