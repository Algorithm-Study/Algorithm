# 초기 변수 설정
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1

# 코인 보다 크거나 같은 경우 코인을 뺀 dp값을 더 해준다
# 코인을 뺀 경우의 dp값에서 코인을 더하면 현재 케이스 코인을 만들 수 있다
for coin in coins:
    for case in range(coin,k+1):
        if case >= coin:
            dp[case] += dp[case-coin]

print(dp[k])