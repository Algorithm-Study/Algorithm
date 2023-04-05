from collections import deque
N, K = map(int, input().split())
max_val = 200001
field = [-1]*(max_val)
queue = deque()
queue.append(N)
field[N] = 0

while queue:
    x = queue.popleft()
    if 2*x < max_val and field[2*x] == -1:
        field[2*x] = field[x] + 1
        queue.append(2*x)
    if x-1 >= 0 and field[x-1] == -1:
        field[x-1] = field[x]+1
        queue.append(x-1)
    if x+1 < max_val and field[x+1] == -1:
        field[x+1] = field[x]+1
        queue.append(x+1)

print(field[K])