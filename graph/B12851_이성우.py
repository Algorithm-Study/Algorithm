from collections import deque

n, k = map(int, input().split())
cnt = [float('inf')]*100_001
q = deque()
q.append(n)
cnt[n] = 0
answer = 0
d = [-1, 1]

while q:
    x = q.popleft()
    if x == k:
        answer += 1
        continue
    
    for nx in (x-1, x+1, x*2):
        if 0 <= nx < 100_001 and cnt[nx] >= cnt[x] + 1:
            cnt[nx] = cnt[x] + 1
            q.append(nx)
        
print(cnt[k])
print(answer)