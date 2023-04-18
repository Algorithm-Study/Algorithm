n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
for idx, dist in enumerate(distance):
    if idx == 0:
        least = cost[idx]
        total = cost[idx] * distance[idx]
        continue
    if least <= cost[idx]:
        total += least*distance[idx]
    else:
        least = cost[idx]
        total += cost[idx] * distance[idx]
print(total)