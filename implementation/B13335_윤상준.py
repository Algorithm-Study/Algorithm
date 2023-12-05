from collections import deque
n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
time = 0
bridges = deque()
while trucks:
    if len(bridges) != w:
        if trucks and trucks[0] + sum(bridges) <= l:
            bridges.append(trucks.popleft())
        else:
            bridges.append(0)
    if len(bridges) == w:
        bridges.popleft()
    time += 1
time += w
print(time)