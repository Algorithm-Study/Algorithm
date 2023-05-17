from collections import deque
import sys
input = sys.stdin.readline

stack = deque(input().rstrip())
deq = deque()

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
    	if stack:
            deq.appendleft(stack.pop())
            
    elif command[0] == 'D':
        if deq:
            stack.append(deq.popleft())
            
    elif command[0] == 'B':
    	if stack:
            stack.pop()
    else:
        stack.append(command[1])
        
print(''.join(stack+deq))