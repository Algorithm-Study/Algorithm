from collections import deque

N, K = map(int, input().split())
dq = deque()
dq.append(N)
board = [0]*100001
ans, cnt = 0, 0

while dq:
    cx = dq.popleft()
    if cx == K:
        ans = board[cx]
        cnt += 1
        continue

    for i in [cx-1, cx+1, cx*2]:
        if 0 <= i < 100001 and (board[i] == 0 or board[i] == board[cx]+1):
            board[i] = board[cx] + 1
            dq.append(i)

print(ans)
print(cnt)