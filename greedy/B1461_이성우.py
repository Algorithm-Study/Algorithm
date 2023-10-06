n, m = map(int, input().split())
arr = list(map(int, input().split()))

plus = [0]
minus = [0]

for a in arr:
    if a > 0:
        plus.append(a)
    else:
        minus.append(-a)
plus.sort(reverse=True)
minus.sort(reverse=True)
answer = 0
for idx, num in enumerate(plus):
    if idx % m == 0:
        answer += num*2

for idx, num in enumerate(minus):
    if idx % m == 0:
        answer += num*2

print(answer - max(plus[0], minus[0]))