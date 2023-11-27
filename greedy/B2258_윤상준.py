n, m = map(int, input().split())
meats = []
for _ in range(n):
    weight, price = map(int, input().split())
    meats.append((price, weight))
meats.sort(key = lambda x: (x[0], -x[1]))
result = []
total_weight, total_cost = 0,0
for i in range(n):
    total_weight += meats[i][1]
    if i >= 1 and meats[i][0] == meats[i-1][0]:
        total_cost += meats[i][0]
    else:
        total_cost = meats[i][0]
    if total_weight >= m:
        result.append(total_cost)
        if meats[i][0] == total_cost:
            break
if not result:
    print(-1)
else:
    print(min(result))