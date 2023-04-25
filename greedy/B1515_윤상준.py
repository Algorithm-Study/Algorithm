from collections import deque
n = list(input())
queue = deque(n)
i = 0
while queue:
    i += 1
    data = list(str(i))
    for d in data:
        if queue[0] == d:
            queue.popleft()
        if len(queue) == 0:
            break
print(i)