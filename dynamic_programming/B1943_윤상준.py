import sys
input = sys.stdin.readline
for _ in range(3):
    n = int(input())
    coins = {}
    total = 0
    for _ in range(n):
        coin, num = map(int, input().split())
        coins[coin] = num
        total += coin*num
    equal = total//2
    if equal != total/2:
        print(0)
        continue
    is_possible = [1] + [0]*equal
    for coin in coins:
        # 내림차순으로 진행해야 함
        for value in range(equal, coin-1, -1):
            if is_possible[value-coin]:
                for j in range(coins[coin]):
                    if value + coin * j <= equal:
                        is_possible[value + coin * j] = 1
    print(is_possible[equal])
        