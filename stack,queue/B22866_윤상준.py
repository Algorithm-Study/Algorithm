import sys
input = sys.stdin.readline
n = int(input())
towers = list(map(int,input().split()))
stack = []
count = [0]*(n+1)
record = [[sys.maxsize,sys.maxsize] for _ in range(n+1)]

for idx, tower in enumerate(towers):
    while len(stack)> 0 and stack[-1][1] <= tower:
        stack.pop()
    count[idx+1] += len(stack)
    if len(stack) > 0 :
        distance = abs(stack[-1][0] - (idx+1))
        # 지점으로부터의 거리가 짧은 경우
        if distance < record[idx+1][1]:
            record[idx+1] = [stack[-1][0], distance]
        # 지점으로부터 거리가 같고 타워 길이가 짧은 경우
        elif distance == record[idx+1][1] and stack[-1][0] < record[idx+1][0]:
            record[idx+1][0] = stack[-1][0]
    stack.append([idx+1,tower])
stack = []
for idx,tower in reversed(list(enumerate(towers))):
    while len(stack) > 0 and stack[-1][1] <=tower:
        stack.pop()
    count[idx+1] += len(stack)
    if len(stack) > 0 :
        distance = abs(stack[-1][0] - (idx+1))
        # 지점으로부터의 거리가 짧은 경우
        if distance < record[idx+1][1]:
            record[idx+1] = [stack[-1][0], distance]
        # 지점으로부터의 거리가 짧은 경우
        elif distance == record[idx+1][1] and stack[-1][0] < record[idx+1][0]:
            record[idx+1][0] = stack[-1][0]
    stack.append([idx+1,tower])

for i in range(1,n+1):
    if count[i]>0:
        print(count[i],record[i][0])
    else:
        print(0)
# 한번에 각 지점 별 거리를 구해야 함