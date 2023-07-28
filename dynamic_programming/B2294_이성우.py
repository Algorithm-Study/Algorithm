n, k = map(int, input().split())
coins = set()
for _ in range(n):
    coin = int(input())
    if coin > k:
        continue
    coins.add(coin)

target = [float('inf')]*(k+1)

for coin in coins:
    target[coin] = 1
    
for coin in coins:
    for i in range(k+1):
        if i + coin <= k:
            target[i+coin] = min(target[i+coin], target[i]+1)

print(-1 if target[k] == float('inf') else target[k])