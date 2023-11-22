from collections import deque
n =int(input())
neg, pos = [], []
for _ in range(n):
    temp = int(input())
    if temp <= 0:
        neg.append(temp)
    else:
        pos.append(temp)
neg.sort()
pos.sort()
queue = deque(neg)
total = 0
while queue:
    if len(queue) > 1:
        total += queue.popleft() * queue.popleft()
    else:
        total += queue.popleft()
while pos:
    if pos[-1] == 1:
        total += pos.pop()
    elif len(pos) > 1:
        if pos[-2] == 1:
            total += pos.pop() + pos.pop()
        else:
            total += pos.pop() * pos.pop()
    else:
        total += pos.pop()
print(total)