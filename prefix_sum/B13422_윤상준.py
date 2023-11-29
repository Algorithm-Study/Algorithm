t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    houses = list(map(int,input().split()))
    if n != m:
        for j in range(m-1):
            houses.append(houses[j])
    count = 0
    total = sum(houses[:m])
    start, end = 0, m
    if total < k:
        count += 1
    while end < len(houses):
        total -= houses[start]
        total += houses[end]
        if total < k:
            count += 1
        start, end = start + 1, end + 1
    print(count)