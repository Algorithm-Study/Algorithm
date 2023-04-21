n = int(input())
local = list(map(int, input().split()))
budget = int(input())
low = 0
high = max(local)
limit = 0
while low <= high:
    mid = (low+ high)//2
    temp = sum([min(x, mid) for x in local])
    if temp == budget:
        print(mid)
        exit(0)
    elif temp > budget:
        high = mid - 1
    else:
        limit = max(limit, mid)
        low = mid + 1
print(limit)