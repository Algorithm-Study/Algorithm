N = int(input())
building = list(map(int, input().split()))
can_see = [0] * N
building_idx = [[float('inf')] * 2 for _ in range(N)]

stack = []
for i, ip in enumerate(building):
    while stack and stack[-1][1] <= ip:
        stack.pop()
    can_see[i] += len(stack)
    if len(stack) > 0:
        dist = abs(stack[-1][0] - i)
        if dist < building_idx[i][1]:
            building_idx[i][0] = stack[-1][0]
            building_idx[i][1] = dist
        elif dist == building_idx[i][1] and stack[-1][0] < building_idx[i][0]:
            building_idx[i][0] = stack[-1][0]
    stack.append((i, ip))

stack = []
for i, ip in reversed(list(enumerate(building))):
    idx = 0
    while stack and stack[-1][1] <= ip:
        stack.pop()
    can_see[i] += len(stack)
    if len(stack) > 0:
        dist = abs(stack[-1][0] - i)
        if dist < building_idx[i][1]:
            building_idx[i][0] = stack[-1][0]
            building_idx[i][1] = dist
        elif dist == building_idx[i][1] and stack[-1][0] < building_idx[i][0]:
            building_idx[i][0] = stack[-1][0]
    stack.append((i, ip))

for i in range(N):
    if can_see[i] == 0:
        print(0)
    else:
        print(can_see[i], building_idx[i][0]+1)

