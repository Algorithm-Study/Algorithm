import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = list(map(int,input().split()))

stack = []
cnt = [0]*(n+1)
near = [[int(1e9), int(1e9)] for _ in range(n+1)]

for idx, v in enumerate(l):
    while len(stack) > 0 and stack[-1][1] <= v:
        stack.pop()
    cnt[idx+1] += len(stack)
    
    if len(stack) > 0 :
        g = abs(stack[-1][0] - (idx+1))
        if g < near[idx+1][1]:
            near[idx+1][0] = stack[-1][0]
            near[idx+1][1] = g
        elif g == near[idx+1][1] and stack[-1][0] < near[idx+1][0]:
            near[idx+1][0] = stack[-1][0]
    stack.append([idx+1, v])

stack = []
for idx, v in reversed(list(enumerate(l))):
    while len(stack) > 0 and stack[-1][1] <= v:
        stack.pop()
    cnt[idx+1] += len(stack)

    if len(stack) > 0 :
        g = abs(stack[-1][0] - (idx+1))
        if g < near[idx+1][1]:
            near[idx+1][0] = stack[-1][0]
            near[idx+1][1] = g
        elif g == near[idx+1][1] and stack[-1][0] < near[idx+1][0]:
            near[idx+1][0] = stack[-1][0]
    stack.append([idx+1, v])

for i in range(1, n+1):
    if cnt[i] > 0:
        print(f'{cnt[i]} {near[i][0]}')
    else:
        print(0)