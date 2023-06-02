from collections import deque

N, K = map(int, input().split())
line = [0 for _ in range(100001)]
dq = deque()
dq.append((N, 0))
line[N] = 1

while dq:
    val, time = dq.popleft()
    if val == K:
        print(time)
        break
    if 0 <= val - 1 and line[val - 1] == 0:
        dq.append((val - 1, time + 1))
        line[val - 1] = 1
    if val * 2 <= 100000 and line[val * 2] == 0:
        dq.appendleft((val * 2, time))
        line[val * 2] = 1
    if val + 1 <= 100000 and line[val + 1] == 0:
        dq.append((val + 1, time + 1))
        line[val + 1] = 1