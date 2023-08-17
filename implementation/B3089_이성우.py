from collections import defaultdict
from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
clover_x = defaultdict(list)
clover_y = defaultdict(list)

for _ in range(n):
    x, y = map(int, input().split())
    clover_x[y].append(x)
    clover_y[x].append(y)

for y in clover_x:
    clover_x[y].sort()
for x in clover_y:
    clover_y[x].sort()
    
x, y = 0, 0

for c in input():
    if c == 'U':
        y = clover_y[x][bisect_right(clover_y[x], y)]
    elif c == 'R':
        x = clover_x[y][bisect_right(clover_x[y], x)]
    elif c == 'D':
        y = clover_y[x][bisect_left(clover_y[x], y)-1]
    else: # c == 'L'
        x = clover_x[y][bisect_left(clover_x[y], x)-1]
    x, y = x, y
    
print(x, y)