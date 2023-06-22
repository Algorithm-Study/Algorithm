n = int(input())

city = []
for _ in range(n):
    x, y = map(int, input().split())
    city.append(y)

stack, cnt = [], 0
for c in city:
    while stack and c <= stack[-1]:
        if c < stack[-1]:
            cnt += 1
        stack.pop()
    stack.append(c)

for s in stack:
    if s != 0:
        cnt += 1
print(cnt)