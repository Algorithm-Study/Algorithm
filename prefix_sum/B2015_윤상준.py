from collections import defaultdict
n,k = map(int, input().split())
data = list(map(int, input().split()))
prefix = defaultdict(int)
# 자기 자신만 선택한 경우 추가
prefix[0] = 1
total = 0
subtotal = 0
for d in data:
    total += d
    if total - k in prefix:
        subtotal += prefix[total-k]
    prefix[total] += 1
print(subtotal)
#목표: prefix[x] - prefix[y] = k (x > y)
# prefix[x]와 k를 알고 있으므로 식을 변형하면
# prefix[x] - k = prefix[y]
# 현재 누적합에서 k를 뺀 이전 누적합이 존재하는지 체크하면 됨