import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    coins = []
    money = 0
    for _ in range(N):
        val, cnt = map(int, input().split())
        coins.append((val, cnt))
        money += val * cnt
    if money % 2 == 1:
        print(0)
        continue
    else:
        dp = [1] + [0] * (money//2)
        for coin, cnt in coins:
            for i in range(money//2, coin-1, -1):
                if dp[i - coin] == 1:
                    for j in range(cnt):
                        if i + j * coin <= money//2:
                            dp[i + j * coin] = 1
    print(dp[money//2])
