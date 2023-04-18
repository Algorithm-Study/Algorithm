from collections import deque


def operator(idx, num):
    if idx == 0:
        return 'D', (num * 2) % 10000
    elif idx == 1:
        return 'S', (num + 9999) % 10000
    elif idx == 2:
        mok = num // 1000
        rem = num % 1000
        return 'L', rem * 10 + mok
    else:
        mok = num // 10
        rem = num % 10
        return 'R', rem * 1000 + mok


def bfs(A, B):
    dq = deque()
    visit = [0 for _ in range(10000)]
    dq.append(([A, '']))
    visit[A] = 1
    while dq:
        cv, stri = dq.popleft()
        for i in range(4):
            dir, nv = operator(i, cv)
            if visit[nv] != 0:
                continue
            if nv == B:
                return stri + dir
            dq.append(([nv, stri + dir]))
            visit[nv] = 1

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))


