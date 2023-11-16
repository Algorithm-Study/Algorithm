from collections import deque
N, K = map(int, input().split())
max_val = 100001
field = [max_val] * max_val
queue = deque()
queue.append(N)
field[N] = 0
count = 1
while queue:
    x = queue.popleft()
    if 2*x == K or x+1 == K or x-1 == K and field[K] != -1:
        if field[x]+1 == field[K]:
            count += 1
    if 2*x < max_val and field[2*x] >= field[x]+1:
        field[2*x] = field[x] + 1
        queue.append(2*x)
    if x-1 >= 0 and field[x-1] >= field[x]+1:
        field[x-1] = field[x] + 1
        queue.append(x-1)
    if x+1 < max_val and field[x+1] >= field[x]+1:
        field[x+1] = field[x] + 1
        queue.append(x+1)
print(field[K])
print(count)