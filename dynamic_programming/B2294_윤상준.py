n, k = map(int, input().split())
dp = [10_001]*10_001
dp[0] = 0
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()
for coin in coins:
    for i in range(coin,10_001):
        dp[i] = min(dp[i], dp[i-coin]+1)
if dp[k] == 10_001:
    print(-1)
else:
    print(dp[k])

# 작은 동전부터 차례대로 dp 갱신
# 현재 가치에서 동전의 가치 뺀 dp에 1을 더해서 진행
