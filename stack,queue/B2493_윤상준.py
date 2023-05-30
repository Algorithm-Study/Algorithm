import sys
input = sys.stdin.readline
n = int(input())
towers = list(map(int, input().split()))
answer = [0]
stack = [[1,towers[0]]]
for idx, tower in enumerate(towers[1:]):
    flag = 0
    while stack:
        if tower < stack[-1][1]:
            answer.append(stack[-1][0])
            flag = 1
            break
        else:
            stack.pop()
    if flag == 0:
        answer.append(0)
    stack.append([idx+2,tower])
        
print(*answer)
# 오큰수와 유사한 문제