from collections import deque

N, a, b = map(int, input().split())
tower = deque()
if a + b - 1 > N:
    print(-1)
else:
    top = max(a, b)
    tower.append(top)
    a_list = deque([i for i in range(1, min(top, a))])
    b_list = deque([i for i in range(min(top, b)-1, 0, -1)])
    if a == 1:
        b_list = deque([1 for _ in range(N - len(tower) - len(a_list) - len(b_list))]) + b_list
    else:
        a_list = deque([1 for _ in range(N - len(tower) - len(a_list) - len(b_list))]) + a_list
    tower = a_list + tower + b_list
    for t in tower:
        print(t, end=" ")
