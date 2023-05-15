t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    profit = 0
    high = 0
    for i in range(n - 1, -1, -1):
        if prices[i] > high:
            high = prices[i]
        else:
            profit += high - prices[i]
    print(profit)