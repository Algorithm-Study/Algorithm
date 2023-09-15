from collections import deque

s = input()
t = input()
visited = set()

q = deque()
q.append(t)
visited.add(t)

while q:
    x = q.popleft()

    if x == s:
        print(1)
        break
    
    for c in range(2):
        if c == 0 and x[-1] == 'A':
            nx = x[:-1]
        elif c == 1 and x[-1] == 'B':
            nx = x[:-1][::-1]
        else:
            continue
        
        if len(nx) >= len(s) and not nx in visited:
            q.append(nx)
            visited.add(nx)
else:
    print(0)