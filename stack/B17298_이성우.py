from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

nums = list(map(int,input().split()))
stack = [0]
answer = deque([])
while nums:
    if nums[-1] >= stack[-1]:
        stack.pop()
        if stack == []:
            answer.appendleft(-1)
            stack.append(nums.pop())
    else:
        answer.appendleft(stack[-1])
        stack.append(nums.pop())
    # print(stack, answer)
    # print(answer)
    
print(*answer)
'''
5
1 2 3 4
>> 2 3 4 -1

6
10 5 4 1
>> -1 -1 -1 -1
'''       