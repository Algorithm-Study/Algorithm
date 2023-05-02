n, k = map(int, input().split())
coins = []
dp = [0 for i in range(k + 1)]
dp[0] = 1
for i in range(n):
    coins.append(int(input()))
for i in coins:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])

# 문제 접근 방법
# # 무엇이 점화식을 이루고 있는지 파악하는 것이 dp의 핵심
# # 자기 자신에서 코인의 값을 하나씩 뺀 곳의 값을 더한 것을 저장