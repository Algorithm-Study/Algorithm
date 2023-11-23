n = int(input())
minus, plus = [], []
ans, minus_max, plus_min = 0, 0, 0

for _ in range(n):
    ip = int(input())
    if ip == 1:
        ans += 1
    elif ip > 0:
        plus.append(ip)
    else:
        minus.append(ip)

minus.sort()
plus.sort(reverse=True)

if len(minus) % 2 == 1:
    minus_max = minus.pop()
if len(plus) % 2 == 1:
    plus_min = plus.pop()

for i in range(0, len(minus), 2):
    ans += minus[i] * minus[i+1]
ans += minus_max

for i in range(0, len(plus), 2):
    ans += plus[i] * plus[i+1]
ans += plus_min

print(ans)
