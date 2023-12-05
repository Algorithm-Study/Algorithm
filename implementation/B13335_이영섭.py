from collections import deque

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
bridge = deque([0 for _ in range(w)])
time = 0

while bridge:
    time += 1
    bridge.popleft()
    if truck:
        if sum(bridge) + truck[0] <= L:
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)
print(time)
