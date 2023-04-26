from collections import deque
n, k = map(int, input().split())
maps = deque(input())

dq = deque(maxlen=k)
dq.append(maps.popleft())
answer = 0
while maps:
    x = maps.popleft()
    if dq and x == 'H' and 'P' in dq:
        dq.remove('P')
        dq.append('X')
        answer += 1
    elif dq and x == 'P' and 'H' in dq:
        dq.remove('H')
        dq.append('X')
        answer += 1
    else:
        dq.append(x)

print(answer)
