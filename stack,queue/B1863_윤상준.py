n = int(input())
stack = []
total = 0
stack.append(tuple(map(int, input().split())))
for _ in range(n-1):
    x, y = map(int, input().split())
    while len(stack) and stack[-1][1] >= y:
        if stack[-1][1] != y:
            total += 1
        stack.pop()
    stack.append((x,y))
while stack:
    if stack[-1][1] != 0:
        total += 1
    stack.pop()
print(total)
# 높이가 변화할 때 높이가 작아지면 pop을 진행해서 스카이라인 갯수를 늘리면 됨
# 알고리즘 개념: Monotone stack(오름차순, 내림차순을 유지한 스택)
# 1. 중복 없는 내림차순 -> 들어가려는 수가 top보다 작거나 같은 경우 pop을 반복
# 2. 중복 없는 오름차순 -> 들어가려는 수가 top보다 크거나 같은 경우 pop을 반복